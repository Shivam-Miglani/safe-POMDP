"""
The `src` package implements tools for safe exploration in finite MDPs. We aim to extend it

Main classes
------------

These classes provide the main functionality for the safe exploration

.. autosummary::
   :template: template.rst
   :toctree:

   SafeMDP
   SafeMDPTU
   link_graph_and_safe_set
   reachable_set
   returnable_set


Grid world
----------

Some additional functionality specific to gridworlds.

.. autosummary::
   :template: template.rst
   :toctree:

   GridWorld
   GridWorldTU
   states_to_nodes
   nodes_to_states
   draw_gp_sample
   grid_world_graph
   grid
   compute_true_safe_set
   compute_true_S_hat
   compute_S_hat0
   shortest_path
   path_to_boolean_matrix
   safe_subpath


Utilities
---------

The following are utilities to make testing and working with the library more
pleasant.

.. autosummary::
   :template: template.rst
   :toctree:

   DifferenceKernel
   max_out_degree
"""