def get_first_cluster(image, k):
    clusters = [[] for _ in range(k)]

    for i in range(len(image)):
        clusters[i % k].append(image[i])
    return clusters


def compress_image_by_k_means(image, k):
    clusters = get_first_cluster(image, k)
    colors = get_average_colors(clusters)
    while True:
        old_colors = colors[:]
        clusters = color_cluster(image, colors)
        colors = get_average_colors(clusters)

        if is_stable(colors, old_colors, 2):
            break
        print(colors)
    return change_colors(image, colors)


def is_stable(colors, old_colors, stable_diff):
    for i in range(len(colors)):
        if get_distance(colors[i], old_colors[i]) > stable_diff:
            return False
    return True


def color_cluster(image, colors):
    colors_len = len(colors)
    clusters = [[] for _ in range(colors_len)]
    for pix in image:
        min_color_diff_index = get_min_color_diff_index(pix, colors, colors_len)
        clusters[min_color_diff_index] += [pix]

    return clusters


def get_min_color_diff_index(pix, colors, colors_len):
    min_dist = None
    min_color = 0
    for i in range(colors_len):
        color = colors[i]
        dist = get_distance(color, pix)
        if min_dist is None or dist < min_dist:
            min_dist, min_color = dist, i
    return min_color


def get_average_colors(clusters):
    colors = []
    for cluster in clusters:
        len_ = len(cluster)
        sum_ = [0, 0, 0]
        avg_ = [0, 0, 0]
        for pixel in cluster:
            for i in range(3):
                sum_[i] += pixel[i]
        for i in range(3):
            if sum_[i] == 0:
                continue
            avg_[i] = sum_[i] // len_

        colors += [tuple(avg_)]
    return colors


def change_colors(image, colors):
    len_ = len(image)
    colors_len = len(colors)
    for i in range(len_):
        min_color_index = get_min_color_diff_index(image[i], colors, colors_len)
        image[i] = colors[min_color_index]
    return image


def get_distance(p1, p2):
    out = 0
    for i in range(len(p1)):
        out += (p1[i] - p2[i]) ** 2
    return out
