# CS7265
big data

Important Links:

https://acadgild.com/blog/decision-tree-python-code

https://www.youtube.com/watch?v=2lEcfRuHFV4

corelation video
https://www.youtube.com/watch?v=2SCg8Kuh0tE

Consensus is a fundamental problem in distributed system. Consensus is a protocol in which
all the computer or nodes collectively agree on a certain value in presesnce of failures.
Paxos algorithm (1978) provided the first fault-tolerant consensus algorithm. Sift is a 
porposed consensus protocol for state machine replication (SMR). In SMR, if a transaction
is valid, a set of inputs will cause the state of the system to transition to the next state.
To keep concurrency, each node has to have same compute and memory resource allocated. This adds 
overhead and reduces throughput. Another method is to use erasure code. it allows each node to
store a part of data that can later be used to reconstruct the original data. But the method adds
high level of complexity. Sift fixes the problem by creating two nodes: CPU node (store state) and passive moemeory node (store consensus log an state machine). This adds a level ofabstraction and reduces redunancy. Traditional Paxos protocols go through software network layersin OS kernels which increases consensus latency. The solution present is remote data memory access
(RDMA). RDMA allows to perform read/ write operation on remote servers. *improvement of F +1
