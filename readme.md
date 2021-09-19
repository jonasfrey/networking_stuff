# tcp
## transmission
## control
## protocol


<table style="display:flex; flex-direction:column; width:1000px" >
    <tr style="display:flex; width:100%">
        <td style="flex:1 1 auto">source port (16bit/2^16/0-65535)</td >
        <td style="flex:1 1 auto">destination port (16bit/2^16/0-65535)</td >
    </tr>
    <tr style="display:flex;">
        <td style="flex:1 1 auto">sequence number (32bit/2^32/0-4294967295)</td >
    </tr>
    <tr style="display:flex;">
        <td style="flex:1 1 auto">acknowledgement number (32bit/2^32/0-4294967295)</td >
    </tr>
    <tr style="display:flex;">
        <td style="flex:1 1 auto">HLEN</td >
        <td style="flex:1 1 auto">MTP</td >
        <td style="flex:1 1 auto">Reserved</td >
        <td style="flex:1 1 auto">Code Bits</td >
        <td style="flex:1 1 auto">Window</td >
    </tr>
    <tr style="display:flex;">
        <td style="flex:1 1 auto">Checksum</td >
        <td style="flex:1 1 auto">Urgent Pointer</td >
    </tr>
    <tr style="display:flex;">
        <td style="flex:1 1 auto">(MLP Flag == 1 -> Last polling data packet) || (MLP flag == 0 -> normal packet)</td >
        <td style="flex:1 1 auto">Padding</td >
    </tr>
    <tr style="display:flex;">
        <td style="flex:1 1 auto">Data</td >
    </tr>
</table>

