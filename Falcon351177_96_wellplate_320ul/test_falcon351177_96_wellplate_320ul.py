import json
from opentrons import protocol_api, types


TEST_LABWARE_SLOT = '5'

RATE = 0.25  # % of default speeds

PIPETTE_MOUNT = 'right'
PIPETTE_NAME = 'p20_single_gen2'

TIPRACK_SLOT = '11'
TIPRACK_LOADNAME = 'opentrons_96_tiprack_20ul'
LABWARE_DEF_JSON = """{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand":{"brand":"Falcon_351177","brandId":["351177"]},"metadata":{"displayName":"Falcon_351177 96 Well Plate 320 µL","displayCategory":"wellPlate","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.5,"yDimension":85.5,"zDimension":14.22},"wells":{"A1":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":14.54,"y":73.94,"z":3.7},"B1":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":14.54,"y":64.94,"z":3.7},"C1":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":14.54,"y":55.94,"z":3.7},"D1":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":14.54,"y":46.94,"z":3.7},"E1":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":14.54,"y":37.94,"z":3.7},"F1":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":14.54,"y":28.94,"z":3.7},"G1":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":14.54,"y":19.94,"z":3.7},"H1":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":14.54,"y":10.94,"z":3.7},"A2":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":23.56,"y":73.94,"z":3.7},"B2":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":23.56,"y":64.94,"z":3.7},"C2":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":23.56,"y":55.94,"z":3.7},"D2":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":23.56,"y":46.94,"z":3.7},"E2":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":23.56,"y":37.94,"z":3.7},"F2":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":23.56,"y":28.94,"z":3.7},"G2":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":23.56,"y":19.94,"z":3.7},"H2":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":23.56,"y":10.94,"z":3.7},"A3":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":32.58,"y":73.94,"z":3.7},"B3":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":32.58,"y":64.94,"z":3.7},"C3":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":32.58,"y":55.94,"z":3.7},"D3":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":32.58,"y":46.94,"z":3.7},"E3":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":32.58,"y":37.94,"z":3.7},"F3":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":32.58,"y":28.94,"z":3.7},"G3":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":32.58,"y":19.94,"z":3.7},"H3":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":32.58,"y":10.94,"z":3.7},"A4":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":41.6,"y":73.94,"z":3.7},"B4":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":41.6,"y":64.94,"z":3.7},"C4":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":41.6,"y":55.94,"z":3.7},"D4":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":41.6,"y":46.94,"z":3.7},"E4":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":41.6,"y":37.94,"z":3.7},"F4":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":41.6,"y":28.94,"z":3.7},"G4":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":41.6,"y":19.94,"z":3.7},"H4":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":41.6,"y":10.94,"z":3.7},"A5":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":50.62,"y":73.94,"z":3.7},"B5":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":50.62,"y":64.94,"z":3.7},"C5":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":50.62,"y":55.94,"z":3.7},"D5":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":50.62,"y":46.94,"z":3.7},"E5":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":50.62,"y":37.94,"z":3.7},"F5":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":50.62,"y":28.94,"z":3.7},"G5":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":50.62,"y":19.94,"z":3.7},"H5":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":50.62,"y":10.94,"z":3.7},"A6":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":59.64,"y":73.94,"z":3.7},"B6":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":59.64,"y":64.94,"z":3.7},"C6":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":59.64,"y":55.94,"z":3.7},"D6":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":59.64,"y":46.94,"z":3.7},"E6":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":59.64,"y":37.94,"z":3.7},"F6":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":59.64,"y":28.94,"z":3.7},"G6":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":59.64,"y":19.94,"z":3.7},"H6":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":59.64,"y":10.94,"z":3.7},"A7":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":68.66,"y":73.94,"z":3.7},"B7":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":68.66,"y":64.94,"z":3.7},"C7":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":68.66,"y":55.94,"z":3.7},"D7":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":68.66,"y":46.94,"z":3.7},"E7":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":68.66,"y":37.94,"z":3.7},"F7":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":68.66,"y":28.94,"z":3.7},"G7":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":68.66,"y":19.94,"z":3.7},"H7":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":68.66,"y":10.94,"z":3.7},"A8":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":77.68,"y":73.94,"z":3.7},"B8":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":77.68,"y":64.94,"z":3.7},"C8":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":77.68,"y":55.94,"z":3.7},"D8":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":77.68,"y":46.94,"z":3.7},"E8":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":77.68,"y":37.94,"z":3.7},"F8":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":77.68,"y":28.94,"z":3.7},"G8":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":77.68,"y":19.94,"z":3.7},"H8":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":77.68,"y":10.94,"z":3.7},"A9":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":86.7,"y":73.94,"z":3.7},"B9":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":86.7,"y":64.94,"z":3.7},"C9":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":86.7,"y":55.94,"z":3.7},"D9":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":86.7,"y":46.94,"z":3.7},"E9":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":86.7,"y":37.94,"z":3.7},"F9":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":86.7,"y":28.94,"z":3.7},"G9":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":86.7,"y":19.94,"z":3.7},"H9":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":86.7,"y":10.94,"z":3.7},"A10":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":95.72,"y":73.94,"z":3.7},"B10":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":95.72,"y":64.94,"z":3.7},"C10":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":95.72,"y":55.94,"z":3.7},"D10":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":95.72,"y":46.94,"z":3.7},"E10":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":95.72,"y":37.94,"z":3.7},"F10":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":95.72,"y":28.94,"z":3.7},"G10":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":95.72,"y":19.94,"z":3.7},"H10":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":95.72,"y":10.94,"z":3.7},"A11":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":104.74,"y":73.94,"z":3.7},"B11":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":104.74,"y":64.94,"z":3.7},"C11":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":104.74,"y":55.94,"z":3.7},"D11":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":104.74,"y":46.94,"z":3.7},"E11":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":104.74,"y":37.94,"z":3.7},"F11":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":104.74,"y":28.94,"z":3.7},"G11":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":104.74,"y":19.94,"z":3.7},"H11":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":104.74,"y":10.94,"z":3.7},"A12":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":113.76,"y":73.94,"z":3.7},"B12":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":113.76,"y":64.94,"z":3.7},"C12":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":113.76,"y":55.94,"z":3.7},"D12":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":113.76,"y":46.94,"z":3.7},"E12":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":113.76,"y":37.94,"z":3.7},"F12":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":113.76,"y":28.94,"z":3.7},"G12":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":113.76,"y":19.94,"z":3.7},"H12":{"depth":10.52,"totalLiquidVolume":320,"shape":"circular","diameter":6.48,"x":113.76,"y":10.94,"z":3.7}},"groups":[{"metadata":{"wellBottomShape":"u"},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"falcon351177_96_wellplate_320ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}"""
LABWARE_DEF = json.loads(LABWARE_DEF_JSON)
LABWARE_LABEL = LABWARE_DEF.get('metadata', {}).get(
    'displayName', 'test labware')
LABWARE_DIMENSIONS = LABWARE_DEF.get('wells', {}).get('A1', {}).get('yDimension')

metadata = {'apiLevel': '2.0'}


def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware(TIPRACK_LOADNAME, TIPRACK_SLOT)
    pipette = protocol.load_instrument(
        PIPETTE_NAME, PIPETTE_MOUNT, tip_racks=[tiprack])

    test_labware = protocol.load_labware_from_definition(
        LABWARE_DEF,
        TEST_LABWARE_SLOT,
        LABWARE_LABEL,
    )

    num_cols = len(LABWARE_DEF.get('ordering', [[]]))
    num_rows = len(LABWARE_DEF.get('ordering', [[]])[0])
    total = num_cols * num_rows
    pipette.pick_up_tip()

    def set_speeds(rate):
        protocol.max_speeds.update({
            'X': (600 * rate),
            'Y': (400 * rate),
            'Z': (125 * rate),
            'A': (125 * rate),
        })

        speed_max = max(protocol.max_speeds.values())

        for instr in protocol.loaded_instruments.values():
            instr.default_speed = speed_max

    set_speeds(RATE)

    pipette.home()
    if(PIPETTE_NAME == 'p20_single_gen2' or PIPETTE_NAME == 'p300_single_gen2' or PIPETTE_NAME == 'p1000_single_gen2' or PIPETTE_NAME == 'p50_single' or PIPETTE_NAME == 'p10_single' or PIPETTE_NAME == 'p300_single' or PIPETTE_NAME == 'p1000_single'):
        if(total > 1):
            #testing with single channel
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]

            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            
            #last well testing
            last_well = (num_cols) * (num_rows)
            well = test_labware.well(last_well-1)
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            set_speeds(RATE)
            #test bottom of last well
            pipette.move_to(well.bottom())
            protocol.pause("If the position is accurate click 'resume.'")
            pipette.blow_out(well)
        else:
            #testing with single channel + 1 well labware
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]

            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            
            #test bottom of first well
            well = test_labware.well('A1')
            pipette.move_to(well.bottom())
            protocol.pause("If the position is accurate click 'resume.'")
            pipette.blow_out(well)
    else:
        #testing for multichannel
        if(total == 96 or total == 384): #testing for 96 well plates and 384 first column
            #test first column
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            
            #test last column
            if(total == 96):
                last_col = (num_cols * num_rows) - num_rows
                well = test_labware.well(last_col)
                all_4_edges = [
                    [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                    [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                    [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                    [well._from_center_cartesian(x=0, y=1, z=1), 'back']
                ]
                for edge_pos, edge_name in all_4_edges:
                    set_speeds(RATE)
                    edge_location = types.Location(point=edge_pos, labware=None)
                    pipette.move_to(edge_location)
                    protocol.pause("If the position is accurate click 'resume.'")
                set_speeds(RATE)
                #test bottom of last column
                pipette.move_to(well.bottom())
                protocol.pause("If the position is accurate click 'resume.'")
                pipette.blow_out(well)
            elif(total == 384):
                #testing for 384 well plates - need to hit well 369, last column
                well369 = (total) - (num_rows) + 1
                well = test_labware.well(well369)
                pipette.move_to(well.top())
                protocol.pause("If the position is accurate click 'resume.'")
                all_4_edges = [
                    [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                    [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                    [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                    [well._from_center_cartesian(x=0, y=1, z=1), 'back']
                ]
                for edge_pos, edge_name in all_4_edges:
                    set_speeds(RATE)
                    edge_location = types.Location(point=edge_pos, labware=None)
                    pipette.move_to(edge_location)
                    protocol.pause("If the position is accurate click 'resume.'")
                set_speeds(RATE)
                #test bottom of last column
                pipette.move_to(well.bottom())
                protocol.pause("If the position is accurate click 'resume.'")
                pipette.blow_out(well)
        elif(num_rows == 1 and total > 1 and LABWARE_DIMENSIONS >= 71.2):
            #for 1 row reservoirs - ex: 12 well reservoirs
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=1, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=1, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=0.75, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            #test last well
            well = test_labware.well(-1)
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=1, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=1, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=0.75, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            set_speeds(RATE)

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
                #test bottom of first well
            pipette.move_to(well.bottom())
            protocol.pause("If the position is accurate click 'resume.'")
            pipette.blow_out(well)

        
        elif(total == 1 and LABWARE_DIMENSIONS >= 71.2 ):
            #for 1 well reservoirs
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=1, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=1, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=0.75, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
                #test bottom of first well
            pipette.move_to(well.bottom())
            protocol.pause("If the position is accurate click 'resume.'")
            pipette.blow_out(well)
        
        else:
            #for incompatible labwares
            protocol.pause("labware is incompatible to calibrate with a multichannel pipette")




    set_speeds(1.0)
    pipette.return_tip()