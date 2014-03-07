Bottleneck configuration
------------------------

Experiment Setup
----------------
This configuration simulates a Tor network in which there are three relays (two non-exit and one exit) and a authority directory server. In this experiment, clients download files of sizes 320 KiB (lightfileclient) and 5 MiB (bulkfileclient) from a web server (fileserver) over the simulated tor network.

Bottleneck in the above network is created by adding a couple of lines to the default relay.torrc file. For each node, create a new file and add the following:

RelayBandwidthRate <bandwidth> KB/MB
MaxAdvertisedBandwidth <bandwidth> KB/MB

where bandwidth = 128 KB for slowrelay and 10 MB for fastrelay. To ensure that the clients form the circuit with the slowrelay as the middle relay, we can leverage the bandwidth weight parameter in the while creating the nodes in the xml file. The scallion plugin takes the b/w weight as an argument and giving the slowrelay's application plugin a smaller value than the fastrelay or exit will ensure that the slowrelay will be chosen as the 2nd hop (middle relay) instead of 1st.

In this experimient setup, there is one light-weight client which downloads 

Rationale
---------



Files to get information about the configuration
------------------------------------------------

1. /home/sim1/gmu-tor/config/bottleneck/data/authoritydata/4uthority/cached-descriptors.new -> for actual bandwidth of the nodes in the network and their weights (for being chosen as a router in the circuit) in the network.
2. In the log file (/home/sim1/gmu-tor/config/bottleneck/data/scallion.log) search for "Bootstrapped 80%". This is point at which the client starts choosing the relays (according to their b/w weights) to form a circuit. A snippet from the log file is show below. Look for the relay nodes which is chosen for hop 1 , hop 2 and the exit node.



0:0:5:927555 [thread-0] 0:15:4:000000000 [tor-message] [bulkfileclient1-59.1.0.0] [scalliontor_logmsg_cb] Bootstrapped 80%: Connecting to the Tor network.
Dec 31 19:15:04.000 [notice] Bootstrapped 80%: Connecting to the Tor network.
Dec 31 19:15:04.000 [debug] void circuit_remove_handled_ports(smartlist_t *)(): Port 80 is not handled.
Dec 31 19:15:04.000 [info] void circuit_predict_and_launch_new()(): Have 0 clean circs (0 internal), need another exit circ.
Dec 31 19:15:04.000 [debug] int new_route_len(uint8_t, extend_info_t *, smartlist_t *)(): Chosen route length 3 (4/4 routers suitable).
Dec 31 19:15:04.000 [info] const node_t *choose_good_exit_server_general(int, int)(): Found 1 servers that might support 0/0 pending connections.
Dec 31 19:15:04.000 [debug] void circuit_remove_handled_ports(smartlist_t *)(): Port 80 is not handled.
Dec 31 19:15:04.000 [debug] const node_t *smartlist_choose_node_by_bandwidth_weights(smartlist_t *, bandwidth_weight_rule_t)(): Got negative bandwidth weights. Defaulting to old selection algorithm.
Dec 31 19:15:04.000 [debug] const node_t *smartlist_choose_node_by_bandwidth(smartlist_t *, bandwidth_weight_rule_t)(): Total weighted bw = 666, exit bw = 1000, nonexit bw = 0, exit weight = 1.000000 (for exit == 1), guard bw = 1000, nonguard bw = 0, guard weight = 0.666667 (for guard == 0)
Dec 31 19:15:04.000 [info] const node_t *choose_good_exit_server_general(int, int)(): Chose exit server '$6290641D9A3CAA6290DEFCA3BE0504AC501E21BE~exit at 54.1.0.0'
Dec 31 19:15:04.000 [debug] int onion_extend_cpath(origin_circuit_t *)(): Path is 0 long; we want 3
Dec 31 19:15:04.000 [debug] const node_t *smartlist_choose_node_by_bandwidth_weights(smartlist_t *, bandwidth_weight_rule_t)(): Got negative bandwidth weights. Defaulting to old selection algorithm.
Dec 31 19:15:04.000 [debug] const node_t *smartlist_choose_node_by_bandwidth(smartlist_t *, bandwidth_weight_rule_t)(): Total weighted bw = 1333, exit bw = 1000, nonexit bw = 1000, exit weight = 0.333333 (for exit == 0), guard bw = 2000, nonguard bw = 0, guard weight = 1.000000 (for guard == 1)
Dec 31 19:15:04.000 [info] const node_t *add_an_entry_guard(const node_t *, int, int)(): Chose $6290641D9A3CAA6290DEFCA3BE0504AC501E21BE~exit at 54.1.0.0 as new entry guard.
Dec 31 19:15:04.000 [info] void log_entry_guards(int)(): exit [6290641D9A3CAA6290DEFCA3BE0504AC501E21BE] (up never-contacted)
Dec 31 19:15:04.000 [debug] const node_t *smartlist_choose_node_by_bandwidth_weights(smartlist_t *, bandwidth_weight_rule_t)(): Got negative bandwidth weights. Defaulting to old selection algorithm.
Dec 31 19:15:04.000 [debug] const node_t *smartlist_choose_node_by_bandwidth(smartlist_t *, bandwidth_weight_rule_t)(): Total weighted bw = 1000, exit bw = 0, nonexit bw = 1000, exit weight = 1.000000 (for exit == 0), guard bw = 1000, nonguard bw = 0, guard weight = 1.000000 (for guard == 1)
Dec 31 19:15:04.000 [info] const node_t *add_an_entry_guard(const node_t *, int, int)(): Chose $F67E278C346268AB43DE50254D8A8F44FFE486A5~fastrelay at 55.1.0.0 as new entry guard.
Dec 31 19:15:04.000 [info] void log_entry_guards(int)(): exit [6290641D9A3CAA6290DEFCA3BE0504AC501E21BE] (up never-contacted),fastrelay [F67E278C346268AB43DE50254D8A8F44FFE486A5] (up never-contacted)
Dec 31 19:15:04.000 [info] const node_t *smartlist_choose_node_by_bandwidth_weights(smartlist_t *, bandwidth_weight_rule_t)(): Empty routerlist passed in to consensus weight node selection for rule weight as guard
Dec 31 19:15:04.000 [info] const node_t *smartlist_choose_node_by_bandwidth(smartlist_t *, bandwidth_weight_rule_t)(): Empty routerlist passed in to old node selection for rule weight as guard
Dec 31 19:15:04.000 [info] const node_t *router_choose_random_node(smartlist_t *, routerset_t *, router_crn_flags_t)(): We couldn't find any live, guard routers; falling back to list of all routers.
Dec 31 19:15:04.000 [debug] const node_t *smartlist_choose_node_by_bandwidth_weights(smartlist_t *, bandwidth_weight_rule_t)(): Got negative bandwidth weights. Defaulting to old selection algorithm.
Dec 31 19:15:04.000 [info] const node_t *add_an_entry_guard(const node_t *, int, int)(): Chose $F456519D90D678620D591F7465033AE1A4C6582B~slowrelay at 56.1.0.0 as new entry guard.
Dec 31 19:15:04.000 [info] void log_entry_guards(int)(): exit [6290641D9A3CAA6290DEFCA3BE0504AC501E21BE] (up never-contacted),fastrelay [F67E278C346268AB43DE50254D8A8F44FFE486A5] (up never-contacted),slowrelay [F456519D90D678620D591F7465033AE1A4C6582B] (not fast/stable, never-contacted)
Dec 31 19:15:04.000 [info] const node_t *smartlist_choose_node_by_bandwidth_weights(smartlist_t *, bandwidth_weight_rule_t)(): Empty routerlist passed in to consensus weight node selection for rule weight as guard
Dec 31 19:15:04.000 [info] const node_t *smartlist_choose_node_by_bandwidth(smartlist_t *, bandwidth_weight_rule_t)(): Empty routerlist passed in to old node selection for rule weight as guard
Dec 31 19:15:04.000 [info] const node_t *router_choose_random_node(smartlist_t *, routerset_t *, router_crn_flags_t)(): We couldn't find any live, guard routers; falling back to list of all routers.
Dec 31 19:15:04.000 [info] const node_t *smartlist_choose_node_by_bandwidth_weights(smartlist_t *, bandwidth_weight_rule_t)(): Empty routerlist passed in to consensus weight node selection for rule weight as middle node
Dec 31 19:15:04.000 [info] const node_t *smartlist_choose_node_by_bandwidth(smartlist_t *, bandwidth_weight_rule_t)(): Empty routerlist passed in to old node selection for rule no weighting
0:0:5:927924 [thread-0] 0:15:4:000000000 [tor-warning] [bulkfileclient1-59.1.0.0] [scalliontor_logmsg_cb] No available nodes when trying to choose node. Failing.
Dec 31 19:15:04.000 [warn] No available nodes when trying to choose node. Failing.
0:0:5:927951 [thread-0] 0:15:4:000000000 [tor-warning] [bulkfileclient1-59.1.0.0] [scalliontor_logmsg_cb] No available nodes when trying to choose node. Failing.
Dec 31 19:15:04.000 [warn] No available nodes when trying to choose node. Failing.
Dec 31 19:15:04.000 [debug] int onion_extend_cpath(origin_circuit_t *)(): Chose router $F67E278C346268AB43DE50254D8A8F44FFE486A5~fastrelay at 55.1.0.0 for hop 1 (exit is exit)
Dec 31 19:15:04.000 [debug] int onion_extend_cpath(origin_circuit_t *)(): Path is 1 long; we want 3
Dec 31 19:15:04.000 [debug] const node_t *choose_good_middle_server(uint8_t, cpath_build_state_t *, crypt_path_t *, int)(): Contemplating intermediate hop: random choice.
Dec 31 19:15:04.000 [info] const node_t *smartlist_choose_node_by_bandwidth_weights(smartlist_t *, bandwidth_weight_rule_t)(): Empty routerlist passed in to consensus weight node selection for rule weight as middle node
Dec 31 19:15:04.000 [info] const node_t *smartlist_choose_node_by_bandwidth(smartlist_t *, bandwidth_weight_rule_t)(): Empty routerlist passed in to old node selection for rule no weighting
Dec 31 19:15:04.000 [info] const node_t *router_choose_random_node(smartlist_t *, routerset_t *, router_crn_flags_t)(): We couldn't find any live, fast routers; falling back to list of all routers.
Dec 31 19:15:04.000 [debug] const node_t *smartlist_choose_node_by_bandwidth_weights(smartlist_t *, bandwidth_weight_rule_t)(): Got negative bandwidth weights. Defaulting to old selection algorithm.
Dec 31 19:15:04.000 [debug] int onion_extend_cpath(origin_circuit_t *)(): Chose router $F456519D90D678620D591F7465033AE1A4C6582B~slowrelay at 56.1.0.0 for hop 2 (exit is exit)
Dec 31 19:15:04.000 [debug] int onion_extend_cpath(origin_circuit_t *)(): Path is 2 long; we want 3
Dec 31 19:15:04.000 [debug] int onion_extend_cpath(origin_circuit_t *)(): Chose router $6290641D9A3CAA6290DEFCA3BE0504AC501E21BE~exit at 54.1.0.0 for hop 3 (exit is exit)
Dec 31 19:15:04.000 [debug] int onion_extend_cpath(origin_circuit_t *)(): Path is complete: 3 steps long



