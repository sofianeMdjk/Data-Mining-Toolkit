from classification_algorithms import load_dataset
from utils import calculate_euclidian_distance, append_unique, extend_unique, distinct_postive_elements_of_list


def get_df_row(dataframe, index):
    row = dataframe.values[index].tolist()[1:]
    return row


def grow_cluster(df, labels, point_index, neighbors, cluster_id, eps, min_points):
    labels[point_index] = cluster_id
    for id_neighbor, neighbor in neighbors:
        if labels[id_neighbor] == -1:
            labels[id_neighbor] = cluster_id
        elif labels[id_neighbor] == 0:
            labels[id_neighbor] = cluster_id
            new_neighbors = get_region_points(df, id_neighbor, eps)
            if len(new_neighbors) >= min_points:
                neighbors = extend_unique(neighbors, new_neighbors)


def get_region_points(df, index, eps):
    neighbors = []
    main_point = get_df_row(df, index)[:-1]
    for num_row, row in df.iterrows():
        point = get_df_row(df, num_row)[:-1]
        print(calculate_euclidian_distance(main_point, point))
        if calculate_euclidian_distance(main_point, point) < eps:
            neighbors = append_unique(neighbors, (num_row, point))
    return neighbors


def run_dbscan(ds_path, eps, min_points):
    dataset = load_dataset(ds_path)
    clusted_id = 0

    # Tells us if the row index has been visited or not (-1 noise point, 0 not visited, else clustered)
    labels = [0] * len(dataset)
    for index, row in dataset.iterrows():
        if labels[index] == 0:
            # point not visited
            neighbor_points = get_region_points(dataset, index, eps)
            print("Neighborhood is : ",neighbor_points)
           # print(neighbor_points)
            if len(neighbor_points) < min_points:
                # This point is considered noise
                labels[index] = -1
            else:
                clusted_id += 1
                grow_cluster(dataset, labels, index, neighbor_points, clusted_id, eps, min_points)

    return labels


#result = run_dbscan("../tmp/temp.csv", 0.5, 5)
#clusters = distinct_postive_elements_of_list(result)
#print("Clusters are : ", clusters)
#print(result)
