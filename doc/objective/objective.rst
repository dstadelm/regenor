#########
Objective
#########

For many embedded projects it is required to define a set of registers. A host application may run on a CPU
communicating with a subsystem running on programmable logic. These days this often is a :term:`SoC` with some ARM CPU
accompanied by a :term:`FPGA`.

The general idea of tools like this one is to have one source for the definition of the registers. From this source the
code for the :term:`FPGA`, the code for the CPU and the documentation shall be generated. Further the source can be used
for additional targets, such as test infrastructure on unit, integration and system test level. To achieve this, the
tool is developed such, that arbitrary plugins can be developed and used.

***************
Why a new tool?
***************

There are industry standard tools that try to solve this problem such as SystemRDL or IP-XACT and certainly others.
These tools use the register level directly as an abstraction level for the definition of the registers. It would be
beneficial to use an abstraction on the function rather then on the implementation. Wouldn't it be preferable if one
could define the values in terms of the function they represent? E.g lets assume a image pipeline in the :term:`FPGA`
containing a gauss filter. Then it would be nice to set the filter size by something representing the module such as
gauss.filter_size and not worrying in about a register address or name that might not even match the contents. This is
the approach of this tool.  Nevertheless the tool allows to write plugins that create SystemRDL or IP-XACT
output due to the open architecture.

********
Glossary
********

.. glossary::

   FPGA
     Field programmable gate array

   SoC
     System on a Chip
