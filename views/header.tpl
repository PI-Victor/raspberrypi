<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ get('title', 'No title')}}</title>

    <!-- Bootstrap -->
    <link href={{get_url('static',filename='css/bootstrap.min.css')}} rel="stylesheet">
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src={{get_url('static',filename='js/bootstrap.min.js')}} rel="stylesheet"></script>

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <div class="container">
      <nav class="navbar navbar-default"  role="navigation">
	<div class="container-fluid">
       	  <ul class="nav nav-pills">
     	    <li class={{get('home', '')}}><a href="/">Home</a></li>
	    <li class={{get('specs', '')}}><a href="/specs">Specs</a></li>
	    <li class={{get('usage', '')}}><a href="/usage">Usage</a></li>	
          </ul>
	</div>
      </nav>
      %include
    </div>
  </body>
</html>
