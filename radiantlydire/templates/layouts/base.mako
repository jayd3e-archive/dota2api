<%namespace name="header" file="header.mako"/>
<%namespace name="footer" file="footer.mako"/>
<!-- base.mako --> 
<!DOCTYPE html>
<html>
    <head>
        <title>${title}</title>
        <link rel="stylesheet" type="text/css" href="/static/css/reset.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/type.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/fonts/trajan/stylesheet.css" charset="utf-8" />

        <!-- JavaScript -->

        <!-- Third-Party Libraries (Order matters) -->
        <script type="text/javascript" src="/static/js/jquery.js"></script>
        <script type="text/javascript" src="/static/js/jquery-ui.js"></script>

        <!-- Application core (Order matters) -->
        <script src="/static/js/app.js"></script>

        <!-- Modules (Order does not matter) -->
        
    </head>
    <body>
        <div class="centered">
            ${header.header(here)}
        </div>
        <div class="body centered">
            ${self.body()}
        </div>
        <div class="footer">
            ${footer.footer()}
        </div>
    </body>
</html>