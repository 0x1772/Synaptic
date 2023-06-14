import dash
import dash_fluentui_components as dfui

app = dash.Dash(__name__)

app.layout = dfui.Card(
    children=[
        dfui.CardBody(
            children=[
                dfui.FluentListTile(
                    title="Package 1",
                    onTap=dfui.FluentCallback(lambda: print("Installing Package 1")),
                ),
                dfui.FluentListTile(
                    title="Package 2",
                    onTap=dfui.FluentCallback(lambda: print("Installing Package 2")),
                ),
            ],
        ),
        dfui.CardFooter(
            children=[
                dfui.FluentFloatingActionButton(
                    child=dfui.FluentIcon(dfui.FluentIcons.add),
                    onPressed=dfui.FluentCallback(lambda: print("Adding Package")),
                ),
            ],
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
