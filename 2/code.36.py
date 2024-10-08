from networkx import DiGraph, all_simple_paths
from typing import Tuple


def function(source: str,
             target: str,
             edge_pairs: list) \
        -> Tuple[int, str]:
    graph, mapping = DiGraph(), {}
    for info in edge_pairs:
        edge_info, weight = info.split(":")
        node_1, node_2 = edge_info.split("->")
        mapping[(node_1, node_2)] = int(weight)
        graph.add_edge(node_1, node_2, weight=int(weight))

    longest_path, distance = max((path for path in all_simple_paths(graph, source, target))), 0
    for former_node, latter_node in zip(longest_path[:-1], longest_path[1:]):
        distance += mapping[(former_node, latter_node)]

    return distance, "->".join(longest_path)


if __name__ == '__main__':
    p_1 = "7"
    p_2 = "36"
    p_3 = [
        "6->28:21",
        "14->29:39",
        "6->24:28",
        "6->26:30",
        "11->37:8",
        "11->32:16",
        "4->40:13",
        "21->32:26",
        "25->40:31",
        "2->9:12",
        "2->3:14",
        "17->22:37",
        "2->5:9",
        "0->33:39",
        "2->17:27",
        "10->37:24",
        "6->18:32",
        "14->25:36",
        "9->16:2",
        "20->30:19",
        "7->29:34",
        "14->20:8",
        "7->9:25",
        "12->25:21",
        "12->27:35",
        "0->27:25",
        "0->24:20",
        "13->38:8",
        "33->41:9",
        "32->36:12",
        "30->33:32",
        "6->7:2",
        "17->40:18",
        "13->29:32",
        "18->21:9",
        "24->36:36",
        "24->30:9",
        "23->39:7",
        "4->18:7",
        "31->32:37",
        "31->33:32",
        "31->35:7",
        "29->30:36",
        "0->40:16",
        "0->36:29",
        "16->33:12",
        "24->29:31",
        "0->31:1",
        "24->25:20",
        "10->33:16",
        "16->38:0",
        "1->29:29",
        "5->10:3",
        "26->32:3",
        "19->31:4",
        "3->5:15",
        "4->39:18",
        "4->38:4",
        "27->34:10",
        "7->10:17",
        "17->18:7",
        "26->29:29",
        "7->19:22",
        "23->24:12",
        "9->21:28",
        "15->31:12",
        "34->37:6",
        "8->12:31",
        "8->11:17",
        "1->4:2",
        "1->2:39",
        "9->35:39",
        "5->6:10",
        "25->31:17",
        "6->32:30",
        "25->33:0",
        "12->41:31",
        "15->24:0",
        "6->40:27",
        "8->22:14",
        "17->34:5",
        "17->35:38",
        "17->33:20",
        "17->30:14",
        "3->35:30",
        "13->14:37",
        "7->34:24",
        "7->31:26"
    ]
    print(function(p_1, p_2, p_3))
