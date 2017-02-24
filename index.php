<!DOCTYPE html>
<html>
<head>
   <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
   
   <!-- <script src="http://192.168.1.83/bs/js/jquery.min.js"></script>
   <script src="http://192.168.1.83/bs/js/bootstrap.js"></script>

   <link  href="http://192.168.1.83/bs/css/bootstrap.css" rel="stylesheet">
   <link href="http://192.168.1.83/bs/style.css" rel="stylesheet" type="text/css">

   <script type="text/javascript" src="http://192.168.1.83/webiopi.js"></script> -->

   <script src="js/jquery.min.js"></script>
   <script src="js/bootstrap.js"></script>

   <link  href="css/bootstrap.css" rel="stylesheet">
   <link href="style.css" rel="stylesheet" type="text/css">

   <!-- <script type="text/javascript" src="webiopi.js"></script> -->

   <script type="text/javascript" src="/webiopi.js"></script>
   
   <script type="text/javascript" src="http://dove.omsk.otpbank.ru/files/weather.js"></script>

   <script type="text/javascript">
      // Запрос температуры myxa
      function getTmp_Myxa(){
         $("#Therm").text(data + " °C");
      }
      // Вызов макроса изменения температуры с интервалом 5 сек.
      setInterval ("callMacro_getTmp0()", 5000);{
      } 
      // Запрос температуры DS18B20
      function callMacro_getTmp0(){
         webiopi().callMacro("getTmp0", [], macro_getTmp0_Callback);
      }
      // Получение температуры DS18B20
      function macro_getTmp0_Callback(macro, args, data) {
         $("#Celsius_0").text(data + " °C");
      }

      // Вызов макроса состояния освещения 2 сек.
      setInterval ("callMacro_fLight()", 2000);{
      }
      function callMacro_fLight(){
        webiopi().callMacro("fLight", [], macro_fLight_Callback);
      }
      function macro_fLight_Callback(macro, args, data) {
         $("#Light").text(data);
      }

      // Вызов макроса изменения времени с интервалом 2 сек.
      setInterval ("callMacro_fTime()", 2000);{
      }
      function callMacro_fTime(){
         webiopi().callMacro("fTime", [], macro_fTime_Callback);
      }
      function macro_fTime_Callback(macro, args, data) {
         $("#TM").text(data);
      }
      // Вызов макроса изменения даты с интервалом 5 сек.
      setInterval ("callMacro_fDate()", 5000);{
      }
      function callMacro_fDate(){
         webiopi().callMacro("fDate", [], macro_fDate_Callback);
      }
      function macro_fDate_Callback(macro, args, data) {
         $("#DT").text(data);
      }
      // Вызов макроса изменения температуры с интервалом 5 сек.
      setInterval ("callMacro_getTemp085()", 5000);{
      }
      // Запрос температуры BMP085
      function callMacro_getTemp085(){
         webiopi().callMacro("getBMP085Temp", [], macro_getTemp085_Callback);
      }
      // Получение температуры BMP085
      function macro_getTemp085_Callback(macro, args, data) {
         $("#Celsius_085").text(data + " °C");
      }
      // Вызов макроса изменения давления с интервалом 5 сек.
      setInterval ("callMacro_getPress085()", 5000);{
      }
      // Запрос давления BMP085
      function callMacro_getPress085(){
         webiopi().callMacro("getBMP085Press", [], macro_getPress085_Callback);
      }
      // Получение давления BMP085
      function macro_getPress085_Callback(macro, args, data) {
         $("#Pressure_085").text(data + " мрс");
      }
      webiopi().ready(function() {
         // Refresh GPIO buttons
         // pass true to refresh repeatedly of false to refresh once
         webiopi().refreshGPIO(true);
      });
   </script>

   <script>
   	function TempGraph() {
   	  document.getElementById('frame_graph').src='./temp085.html'
   	}
   </script>

   <script>
   	function PressGraph() {
   	  document.getElementById('frame_graph').src='./press085.html'
   	}
   </script>

   <script>
      function OutTempGraph() {
        document.getElementById('frame_graph').src='./outtemp.html'
      }
   </script>

   <script>
      function HumiSHTGraph() {
        document.getElementById('frame_graph').src='./humiSHT.html'
      }
   </script>

   <script>
      function TempSHTGraph() {
        document.getElementById('frame_graph').src='./tempSHT.html'
      }
   </script> 

   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <title>Room</title>
   <meta name="description" content="">
   <meta name="keywords" content="">
   <link rel="shortcut icon" href="/favicon.ico">
</head>

<body>

<!--
<h1>
<div class="container">
  <div class="row">
    <div>111</div>
  </div>
</div>
</h1>

<h2>
<div class="container">
   <div class="row">
      <div>111</div>  
   </div>
</div>
</h2>
-->

<table border=0 cellspacing=0 cellpadding=0 width=280px align="center">
   <tr>
      <td width=50% align="left">
         <div class="label label-primary norm_text" id="DT" align="center"></div>        
      </td>
      <td width=50% align="right">
         <!-- <div class="label label-primary norm_text" id="Celsius_0" align="center"></div> -->
         <div class="label label-primary norm_text" align="center" onClick="OutTempGraph()">
            <!-- <script type="text/javascript">document.write(Therm)</script>&deg; °C</div> -->
            <script type="text/javascript">document.write(Therm)</script> °C</div>
      </td>
   </tr>
</table>

<table border=0 cellspacing=0 cellpadding=0 width=280px align="center">
   <tr>
      <td width=50% align="left">
         <div class="label label-primary norm_text" id="Light" align="center">light</div>        
      </td>
      <td width=50% align="right">
         <!-- <div class="label label-primary norm_text" id="Celsius_0" align="center"></div> -->
         <div class="label label-primary norm_text" align="center" onClick="OutTempGraph()">
            <!-- <script type="text/javascript">document.write(Therm)</script>&deg; °C</div> -->
            <script type="text/javascript">document.write(Therm)</script> °C</div>
      </td>
   </tr>
</table>

<table border=0 cellspacing=0 cellpadding=0 width=100%>
   <tr>
      <td width=10%>&nbsp;&nbsp;&nbsp;</td>
   </tr>
   <tr>
      <td width=10%>&nbsp;&nbsp;&nbsp;</td>
   </tr>
   <tr>
      <td width=10%>&nbsp;&nbsp;&nbsp;</td>
      <td width=80% align="center">
         <div class="label label-primary sbig_text" id="TM" align="center"></div>
      </td>
      <td width=10%>&nbsp;&nbsp;&nbsp;</td>
   </tr>
   <tr>
      <td width=10%>&nbsp;&nbsp;&nbsp;</td>
   </tr>
   <tr>
      <td width=10%>&nbsp;&nbsp;&nbsp;</td>
   </tr>
   </table>

   <table border=0 cellspacing=0 cellpadding=0 width=280px align="center">
   <tr>
      <td width=50% align="left">
         <div class="label label-primary norm_text" id="Pressure_085" align="center" onClick="PressGraph()"></div>
      </td>
      <td width=50% align="right">
         <div class="label label-primary norm_text" id="Celsius_085" align="center" onClick="TempGraph()"></div>
      </td>
   </tr>
   <tr>
      <td width=50%>&nbsp;&nbsp;&nbsp;</td>
      <td width=50%>&nbsp;&nbsp;&nbsp;</td>
   </tr>
</table>

<table border=0 cellspacing=0 cellpadding=0 width=280px align="center">
   <tr>
      <td width=50% align="left">
         <div class="label label-primary norm_text" id="HumiSHT" align="center" onClick="HumiSHTGraph()">humi</div>
      </td>
      <td width=50% align="right">
         <div class="label label-primary norm_text" id="TempSHT" align="center" onClick="TempSHTGraph()">temp</div>
      </td>
   </tr>
   <tr>
      <td width=50%>&nbsp;&nbsp;&nbsp;</td>
      <td width=50%>&nbsp;&nbsp;&nbsp;</td>
   </tr>
</table>

<table border=0 cellspacing=0 cellpadding=0 width=100%>
	<tr>
	  <td width=100% align="center">
			<iframe 
				src='outtemp.html'
				id='frame_graph' 
				name='frame_graph' 
				frameborder=0
				scrolling=auto 
				style='margin-left: 0; width: 100%; height: 250px;'>
			</iframe>
		</td>
	</tr>
</table>
<div id="Therm"></div>
</body>  
</html>
