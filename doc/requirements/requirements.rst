############
Requirements
############

.. req:: Input Data Form
   :id: REQ000
   :status: open
   :tags: input;interface
   :collapse: True

   The register definition created by the user shall be in human readable form.

.. req:: Version Control
   :id: REQ001
   :status: open
   :tags: vcs;version;control
   :collapse: True

   The register definition input data shall be in a form that it is compatible with common version control systems.

.. req:: Editor / IDE support
   :id: REQ002
   :status: open
   :tags: ide;editor
   :collapse: True

   The format of the register definition input data shall provide means to support the user creating the register
   definitions. Ideally this support is provided by LSP to make it IDE/Editor agnostic.

.. req:: 2 Level Muxing
   :id: REQ003
   :status: open
   :tags: pipelining;map;bank
   :collapse: True

   One target for generators is specifically FPGAs. From experience it is beneficial if the multiplexers can be
   distributed across two levels. This allows better pipelining. We introduce the words *Map* and *Bank* for this sake.
   A *Map* contains an configurable arbitrary number of *Banks*. Each *Bank* can contain any number of *Registers* up to
   the configurable maximum of *Registers* per *Bank*.

.. req:: Modular Map/Bank creation
   :id: REQ004
   :status: open
   :tags: map;bank;modular
   :collapse: True

   Input and output plugins shall allow partial regeneration.

.. req:: Declaration support
   :id: REQ005
   :status: open
   :tags: declaration
   :collapse: True

   Support for declarations of any element in the register description format, such that the declaration can be used
   throughout as instance. Like a class and instances of that class.

.. req:: Includes
   :id: REQ006
   :status: open
   :tags: include
   :collapse: True

   The input format shall allow includes such that the register definition input data can be split into multiple files.

.. req:: Abstraction
   :id: REQ007
   :status: open
   :tags: abstraction
   :collapse: True

   The register definition input data shall rely on the abstraction of modules and their parameter fields not actual
   registers.

.. req:: Memories
   :id: REQ008
   :status: open
   :tags: memories
   :collapse: True

   Memory mapped regions (attached RAM in the FPGA) shall be supported

.. req:: Arrays
   :id: REQ009
   :status: open
   :tags: arrays
   :collapse: True

   Arrays shall be supported on any level of the abstraction.

.. req:: Unsigned Values
   :id: REQ010
   :status: open
   :tags: Unsigned;integer
   :collapse: True

   Unsigned values in fix point format shall be supported.

.. req:: Signed Values
   :id: REQ011
   :status: open
   :tags: signed;integer
   :collapse: True

   Signed values in fix point format shall be supported.

.. req:: Bitfield Values
   :id: REQ012
   :status: open
   :tags: bitfield;std_logic_vector
   :collapse: True

   Bitfields with no actual mathematical representation shall be supported.

.. req:: Bit Values
   :id: REQ013
   :status: open
   :tags: bit;std_logic
   :collapse: True

   Single bit values shall be supported. These shall allow boolean values where True is mapped to logical '1' and False
   is mapped to logical '0'.

.. req:: Plugin Architecture
   :id: REQ014
   :status: open
   :tags: plugin
   :collapse: True

   The tool shall be implemented using a plugin architecture. All the plugins are dependent on the model. The model does
   not know about the plugins. Everything but the model is a plugin. Therefor the parser is a plugin, as are generators
   creating output artefacts.

.. req:: Address Pinning
   :id: REQ015
   :status: open
   :tags: pinning;address
   :collapse: True

   It shall be possible to define the address of the register in which the value field lies in. This shall be an
   optional parameter.

.. req:: Bit Pinning
   :id: REQ016
   :status: open
   :tags: pinning;bit
   :collapse: True

   It shall be possible to define the LSB of the value field in the register. This shall be an optional parameter.

.. req:: Permission
   :id: REQ017
   :status: open
   :tags: permission
   :collapse: True

   It shall be possible to define the permission of the value field e.g. [read, write, read and write].

   .. note:: Default shall be read and write.

.. req:: Stickyness
   :id: REQ018
   :status: open
   :tags: stickyness
   :collapse: True

   It shall be possible define if a value field is sticky or not. E.g. an error bit usually is sticky, once
   a error has occured the bit indicating that this error has occured should persist.

   .. note:: Default shall be not sticky.

.. req:: Sticky clear behaviour
   :id: REQ019
   :status: open
   :tags: clear;stickyness
   :collapse: True

   It shall be possible to define how a sticky field is cleared. E.g. clear when the field is read, or clear when the
   field is written to, or no clear.

   .. note:: Default shall be no clear.

.. req:: Readback behaviour
   :id: REQ020
   :status: open
   :tags: readback
   :collapse: True

   It shall be possible to define the readback behaviour of a "read and write" value field. The value written to
   the register is read back or reading is independent of the write. E.g. a counter can be set to a defined value and
   when read the current value of the value is read back.

   .. note:: Default value shall be readback of written value
