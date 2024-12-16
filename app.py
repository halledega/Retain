from nicegui import ui

from Retaining_Wall import *

concrete = Concrete(name = 'C90')
soil = Soil('Soil', 19.0, 0.33, 1.0, 3.0, 300.0, 200.0, 0.35)
wall = Wall('Wall', 1200.0, 200.0, 300.0, 250.0, 900.0, 400.0)

class exp(ui.expansion):
    def __init__(self, text = '', *, caption = None, icon = None, group = None, value = False, on_value_change = None):
        super().__init__(text, caption=caption, icon=icon, group=group, value=value, on_value_change=on_value_change)
@ui.page('/') #index page
def page_layout():
    with ui.tabs().classes('left-0 top-0') as tabs:
        loads_tab = ui.tab('Loads').classes('bg-gray-100 rounded')
        geo_tab = ui.tab('Geotechnical').classes('bg-gray-100 rounded')
        struct_tab = ui.tab('Structural').classes('bg-gray-100 rounded')
        reort_tab = ui.tab('Report').classes('bg-gray-100 rounded')
    with ui.tab_panels(tabs, value=loads_tab).classes('w-full'):
        with ui.tab_panel(loads_tab):
            ui.label('Loads')
        with ui.tab_panel('Geotechnical'):
            ui.label('Geotechnical Checks')
    with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-stretch'):
        ui.label('HEADER')
    with ui.left_drawer(fixed=False).style('background-color: #d7e3f4') as left_drawer:
        # Soil properties
        with ui.expansion('Soil Properties', group='inputs').classes('w-full') as soil:
            with ui.column().classes('w-full'):
                # ULS bearing pressure
                ui.input(label='ULS Bearing (kPa)').bind_value(soil, 'Q_uls').classes('w-full')
                # SLS bearing pressure 
                ui.input(label='SLS Bearing (kPa)').bind_value(soil, 'Q_sls').classes('w-full')
                # Density
                ui.input('Unit Weight (kN/m3)').bind_value(soil, 'Density')
                # ka
                ui.input('Active Pressure Coefficient').bind_value(soil, 'ka')
                # ko
                ui.input('At Rest Pressure Coefficient').bind_value(soil, 'ko')
                # kp
                ui.input('Passive Pressure Coefficient').bind_value(soil, 'kp')
                # mu
                ui.input('Friction Coefficient').bind_value(soil, 'Mu')
                # Max DC ratio for bearing
                ui.input(label='Design Ratio', value=0.99).classes('w-full')
        with ui.expansion('Concrete Properties', group='inputs').classes('w-full') as conc:
            with ui.column().classes('w-full'):
                # Dropdown to select concrete name
                ui.label('Select Concrete Type').classes('w-full')
                conc_select = ui.select(['C25', 'C30', 'C35', 'C40', 'C45'], value='C25').bind_value_to(concrete, 'Name').classes('w-full')
                # Display fc as read-only
                ui.input('fc (MPa)', value=concrete.fc).bind_value(concrete, 'fc').props('readonly').classes('w-full')
                # Display phi as read-only
                ui.input('phi', value=concrete.phi).bind_value(concrete, 'phi').props('readonly').classes('w-full')
                # Display density as read-only
                ui.input('Density', value=concrete.Density).bind_value(concrete, 'Density').props('readonly').classes('w-full')
                # Display alpha1 as read-only label
                ui.input('alpha1', value=round(concrete.alpha1,2)).bind_value(concrete, 'alpha1').props('readonly').classes('w-full')
                # Display beta1 as read-only label
                ui.input('beta1', value=round(concrete.beta1,2)).bind_value(concrete, 'beta1').props('readonly').classes('w-full')
        with ui.expansion('Rebar Properties', group='inputs').classes('w-full') as rebar:
            with ui.column().classes('w-full').classes('w-full'):
                ui.input(label='Phu Facotr', placeholder='0.85', value='0.85').classes('w-full')
                ui.input(label='Yield Strength (MPa)', placeholder='400', value='400').classes('w-full')
        with ui.expansion('Wall Dimensions', group='inputs').classes('w-full') as wall:
            with ui.column().classes('w-full'):
                h = ui.input('Height (mm)').bind_value(wall, 'Height')
                tw = ui.input('Thickness (mm)').bind_value(wall, 'Wall_Thickness')
                b = ui.input('Footing Length (mm)').bind_value(wall, 'Footing_Length')
                toe = ui.input('Toe Length (mm)').bind_value(wall, 'Toe_Length')
                heel = ui.input('Heel Length (mm)').props('readonly')
                D = ui.input('Footing Thickness (mm)').bind_value(wall, 'Footing_Thickness')
                tc = ui.input('Toe Cover (mm)').bind_value(wall, 'Toe_Cover')
        ui.button("Run Wall").classes('w-full')
        ui.button("Save").classes('w-full')
        ui.button("Export Report").classes('w-full')
    with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
        ui.label('RIGHT DRAWER')
    with ui.footer().style('background-color: #3874c8'):
        ui.label('FOOTER')
ui.run()