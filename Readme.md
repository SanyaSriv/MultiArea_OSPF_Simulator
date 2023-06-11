# <span style="text-decoration:underline;">Multi-Area OSPF Simulator</span>



1. **Aim of The Project**

    The aim of this project is to simulate how different types of LSAs (LSA 1, LSA 3, LSA 4, and LSA 5) travel across a multi-area topology. Instead of focusing on how the packets look like and the data they contain (the IP addresses or the MAC addresses), this project focuses more on a higher-level view of how different LSAs reach the routers and how they flow. There are some limitations of this project which have been discussed in the sections later on.

2. **Technology Used**

    This project has been programmed in Python. The library PyGame has been used to develop the topography and interactive user interface. All the code has been pushed to a private GitHub repository: [https://github.com/SanyaSriv/MultiArea_OSPF_Simulator](https://github.com/SanyaSriv/MultiArea_OSPF_Simulator)

3. **Description of the Topology**

    We have 3 different areas:

    Area 1: This has 6 internal routers and is connected to the backbone area through an ABR.

    Area 2: This is our backbone area. It has 4 routers and 2 ABRs. Router 7 is an ASBR, as it is connected to an ISP.

    Area 3: This is a stubby area. It has 3 routers and an ABR (router 11), which connects it to the backbone area.


4. **Working with the Simulation**

    There are different buttons that are responsible for different kinds of simulations. 
    
    The LSA packets are represented by triangles that travel across the routers. When a simulation button is clicked, the triangles travel across the routers, and every router has a designated color, so all the triangles originating from it will have that color.
  
    **Send LSA1**: This button simulates all LSA 1 traversal

    **Clear LSA1 text**: This button clears the text displayed by LSA 1s traversal.

    **Single LSA3**: This button simulates a single LSA 3 traversal. There would be multiple LSA 3 packets all over, but this button is to simulate how a single LSA 3 would travel from the ABRs into the 3 areas This does not show all the LSA 3 traversals. If we want to see all LSA 3 packets, then we would have to use the master simulation button. For this, we assume that ABR 1 has received 1 LSA 1 from area 1 and 1 LSA1 from area 2. Similarly, ABR 2 has received 1 LSA 1 from Area 3 and 1 LSA 1 from Area 2. Now both these ABRs send out 1 LSA3 in the respective areas.  

    **Clear LSA3 text**: This button clears the text displayed by LSA 3s.

    **Send LSA4**: This button simulates LSA 4 traversal. The ASBR (Router 7) sends its LSA 4, which is received by ABR 1. The ABR 1 sends out an LSA 4 for this in area 1. These do not get forwarded into Area 3 as it is a stubby area.

    **Clear LSA4 text**: This button clears the text displayed by LSA 4s.

    **Send LSA5**: This button simulates LSA 5 traversal.

    **Clear LSA5 text**: This button clears the text displayed by LSA 5s.

    **Master Simulation**: to simulate all the packet traversals together (LSA 1, LSA 3, LSA 4, LSA5). All text alongside the routers for all LSA 1s is in black; for all LSA 3s in red; for LSA 4s in blue; and for LSA 5s in green.

    **Clear Master Simulation**: This button clears all the text displayed by Master Simulation.

    **Display separate LSA 3s**: This button is specific to the master simulation, and it is a toggle button. It is used to display the information about the router that sent the LSA 3 packet in the master simulation. Without this turned on, we would just see a message like 'Received LSA 3: area 1'. So even if a router in area 1 receives multiple LSA 3s from area 2, it would just display 1 single text: 'Received LSA 3: area 1'. With this feature turned on, we would see which router sent the LSA 3 that was received by a router in area 1. So instead of this text: 'Received LSA 3: area 1', we will see a more elaborate text such as: ‘'Received LSA 3: area 1: Router 8'. This would mean that this router received an LSA 3, which was originally an LSA 1 from router 8 and was converted into an LSA 3 by the ABR. 

    **Display Shortened Texts**: This button is specific to the master simulation, and it is a toggle button as well. It is used to display shorter strings for the master simulation so everything is clearly visible and texts do not overlap. Even after using this, we still might see some texts overlapping, but it is able to display information more clearly with lesser text overlaps.

5. **Limitations of this project**

    The following are some of the limitations of this project:

    1. The topology used in this project does not convey any information about the IP addresses. We have not labeled any IP addresses because we have focused on LSA traversals on a higher and more abstract level. Hence, this project and simulation are unable to provide information about what the different LSA packets look like and what is their destination and source IP addresses. Instead of saying that an LSA travels from this x IP source to y IP destination address, we say that it travels from router x to router y. All the other details are abstracted and not shown.
    2. We do not have any switches in the topology, because of which using a DR/BDR was not necessary. Hence, this project does not demonstrate packet traversal when there is a DR/BDR. For this reason, the traversal of LSA type 2 is skipped in this simulation.
    3. This project does not demonstrate how a totally stubby area behaves. We just have the simulation for a stubby area. 
    4. This simulation also does not contain injecting the default routes into the areas. 
