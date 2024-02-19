<?php
    // Conectando ao banco
    $servidor = 'localhost';
    $usuario = 'root';
    $senha = '';
    $banco = 'sentinela';

    $link = mysqli_connect($servidor, $usuario, $senha, $banco);

    // Salvar dados
    // $dig = json_decode($_POST['dig']);
    // $mou = json_decode($_POST['mouse']);
    // $comp = json_decode($_POST['comp']);

    $dig = json_decode('{"1":{"tecla":"d","pos":"KeyD","evento":"keydown","campo":"txtNum","ts":"2023-11-04 20:03:10:000738","epoch":1699138990738},"2":{"tecla":"w","pos":"KeyW","evento":"keydown","campo":"txtNum","ts":"2023-11-04 20:03:10:000802","epoch":1699138990802},"3":{"tecla":"a","pos":"KeyA","evento":"keydown","campo":"txtNum","ts":"2023-11-04 20:03:10:000842","epoch":1699138990842},"4":{"tecla":"d","pos":"KeyD","evento":"keyup","campo":"txtNum","ts":"2023-11-04 20:03:10:000866","epoch":1699138990866},"5":{"tecla":"w","pos":"KeyW","evento":"keyup","campo":"txtNum","ts":"2023-11-04 20:03:10:000946","epoch":1699138990946},"6":{"tecla":"a","pos":"KeyA","evento":"keyup","campo":"txtNum","ts":"2023-11-04 20:03:10:000962","epoch":1699138990962},"7":{"tecla":"d","pos":"KeyD","evento":"keydown","campo":"txtNum","ts":"2023-11-04 20:03:10:000962","epoch":1699138990962},"8":{"tecla":"w","pos":"KeyW","evento":"keydown","campo":"txtMes","ts":"2023-11-04 20:03:11:000050","epoch":1699138991050},"9":{"tecla":"d","pos":"KeyD","evento":"keyup","campo":"txtMes","ts":"2023-11-04 20:03:11:000074","epoch":1699138991074},"10":{"tecla":"a","pos":"KeyA","evento":"keydown","campo":"txtMes","ts":"2023-11-04 20:03:11:000075","epoch":1699138991075},"11":{"tecla":"a","pos":"KeyA","evento":"keyup","campo":"txtMes","ts":"2023-11-04 20:03:11:000154","epoch":1699138991154},"12":{"tecla":"w","pos":"KeyW","evento":"keyup","campo":"txtMes","ts":"2023-11-04 20:03:11:000162","epoch":1699138991162},"13":{"tecla":"d","pos":"KeyD","evento":"keydown","campo":"txtMes","ts":"2023-11-04 20:03:11:000162","epoch":1699138991162},"14":{"tecla":"w","pos":"KeyW","evento":"keydown","campo":"txtMes","ts":"2023-11-04 20:03:11:000266","epoch":1699138991266},"15":{"tecla":"a","pos":"KeyA","evento":"keydown","campo":"txtMes","ts":"2023-11-04 20:03:11:000282","epoch":1699138991282},"16":{"tecla":"d","pos":"KeyD","evento":"keyup","campo":"txtAno","ts":"2023-11-04 20:03:11:000302","epoch":1699138991302},"17":{"tecla":"a","pos":"KeyA","evento":"keyup","campo":"txtAno","ts":"2023-11-04 20:03:11:000362","epoch":1699138991362},"18":{"tecla":"d","pos":"KeyD","evento":"keydown","campo":"txtAno","ts":"2023-11-04 20:03:11:000362","epoch":1699138991362},"19":{"tecla":"w","pos":"KeyW","evento":"keyup","campo":"txtAno","ts":"2023-11-04 20:03:11:000371","epoch":1699138991371},"20":{"tecla":"w","pos":"KeyW","evento":"keydown","campo":"txtAno","ts":"2023-11-04 20:03:11:000474","epoch":1699138991474},"21":{"tecla":"a","pos":"KeyA","evento":"keydown","campo":"txtAno","ts":"2023-11-04 20:03:11:000498","epoch":1699138991498},"22":{"tecla":"d","pos":"KeyD","evento":"keyup","campo":"txtAno","ts":"2023-11-04 20:03:11:000506","epoch":1699138991506},"23":{"tecla":"a","pos":"KeyA","evento":"keyup","campo":"txtAno","ts":"2023-11-04 20:03:11:000594","epoch":1699138991594},"24":{"tecla":"w","pos":"KeyW","evento":"keyup","campo":"txtAno","ts":"2023-11-04 20:03:11:000610","epoch":1699138991610},"25":{"tecla":"d","pos":"KeyD","evento":"keydown","campo":"txtAno","ts":"2023-11-04 20:03:11:000610","epoch":1699138991610},"26":{"tecla":"w","pos":"KeyW","evento":"keydown","campo":"txtAno","ts":"2023-11-04 20:03:11:000722","epoch":1699138991722},"27":{"tecla":"d","pos":"KeyD","evento":"keyup","campo":"txtAno","ts":"2023-11-04 20:03:11:000746","epoch":1699138991746},"28":{"tecla":"a","pos":"KeyA","evento":"keydown","campo":"txtAno","ts":"2023-11-04 20:03:11:000762","epoch":1699138991762},"29":{"tecla":"a","pos":"KeyA","evento":"keyup","campo":"txtAno","ts":"2023-11-04 20:03:11:000834","epoch":1699138991834},"30":{"tecla":"d","pos":"KeyD","evento":"keydown","campo":"txtAno","ts":"2023-11-04 20:03:11:000842","epoch":1699138991842},"31":{"tecla":"w","pos":"KeyW","evento":"keyup","campo":"txtAno","ts":"2023-11-04 20:03:11:000850","epoch":1699138991850},"32":{"tecla":"d","pos":"KeyD","evento":"keyup","campo":"txtAno","ts":"2023-11-04 20:03:11:000978","epoch":1699138991978},"33":{"tecla":"w","pos":"KeyW","evento":"keydown","campo":"txtAno","ts":"2023-11-04 20:03:11:000978","epoch":1699138991978},"34":{"tecla":"d","pos":"KeyD","evento":"keydown","campo":"txtCVC","ts":"2023-11-04 20:03:12:000090","epoch":1699138992090},"35":{"tecla":"w","pos":"KeyW","evento":"keyup","campo":"txtCVC","ts":"2023-11-04 20:03:12:000122","epoch":1699138992122},"36":{"tecla":"w","pos":"KeyW","evento":"keydown","campo":"txtCVC","ts":"2023-11-04 20:03:12:000202","epoch":1699138992202},"37":{"tecla":"d","pos":"KeyD","evento":"keyup","campo":"txtCVC","ts":"2023-11-04 20:03:12:000210","epoch":1699138992210},"38":{"tecla":"a","pos":"KeyA","evento":"keydown","campo":"txtCVC","ts":"2023-11-04 20:03:12:000234","epoch":1699138992234},"39":{"tecla":"a","pos":"KeyA","evento":"keyup","campo":"txtCVC","ts":"2023-11-04 20:03:12:000306","epoch":1699138992306},"40":{"tecla":"d","pos":"KeyD","evento":"keydown","campo":"txtCVC","ts":"2023-11-04 20:03:12:000307","epoch":1699138992307},"41":{"tecla":"w","pos":"KeyW","evento":"keyup","campo":"txtCVC","ts":"2023-11-04 20:03:12:000346","epoch":1699138992346},"42":{"tecla":"w","pos":"KeyW","evento":"keydown","campo":"txtCVC","ts":"2023-11-04 20:03:12:000410","epoch":1699138992410},"43":{"tecla":"d","pos":"KeyD","evento":"keyup","campo":"txtCVC","ts":"2023-11-04 20:03:12:000442","epoch":1699138992442},"44":{"tecla":"a","pos":"KeyA","evento":"keydown","campo":"txtCVC","ts":"2023-11-04 20:03:12:000450","epoch":1699138992450},"45":{"tecla":"a","pos":"KeyA","evento":"keyup","campo":"txtCVC","ts":"2023-11-04 20:03:12:000570","epoch":1699138992570},"46":{"tecla":"w","pos":"KeyW","evento":"keyup","campo":"txtCVC","ts":"2023-11-04 20:03:12:000586","epoch":1699138992586},"47":{"tecla":"d","pos":"KeyD","evento":"keydown","campo":"txtCVC","ts":"2023-11-04 20:03:12:000586","epoch":1699138992586},"48":{"tecla":"d","pos":"KeyD","evento":"keyup","campo":"txtNom","ts":"2023-11-04 20:03:12:000738","epoch":1699138992738},"49":{"tecla":"w","pos":"KeyW","evento":"keydown","campo":"txtNom","ts":"2023-11-04 20:03:12:000738","epoch":1699138992738},"50":{"tecla":"a","pos":"KeyA","evento":"keydown","campo":"txtNom","ts":"2023-11-04 20:03:12:000747","epoch":1699138992747},"51":{"tecla":"a","pos":"KeyA","evento":"keyup","campo":"txtNom","ts":"2023-11-04 20:03:12:000858","epoch":1699138992858},"52":{"tecla":"d","pos":"KeyD","evento":"keydown","campo":"txtNom","ts":"2023-11-04 20:03:12:000858","epoch":1699138992858},"53":{"tecla":"w","pos":"KeyW","evento":"keyup","campo":"txtNom","ts":"2023-11-04 20:03:12:000874","epoch":1699138992874},"54":{"tecla":"w","pos":"KeyW","evento":"keydown","campo":"txtNom","ts":"2023-11-04 20:03:12:000962","epoch":1699138992962},"55":{"tecla":"a","pos":"KeyA","evento":"keydown","campo":"txtNom","ts":"2023-11-04 20:03:12:000971","epoch":1699138992971},"56":{"tecla":"d","pos":"KeyD","evento":"keyup","campo":"txtNom","ts":"2023-11-04 20:03:12:000994","epoch":1699138992994},"57":{"tecla":"a","pos":"KeyA","evento":"keyup","campo":"txtNom","ts":"2023-11-04 20:03:13:000074","epoch":1699138993074},"58":{"tecla":"w","pos":"KeyW","evento":"keyup","campo":"txtNom","ts":"2023-11-04 20:03:13:000082","epoch":1699138993082},"59":{"tecla":"d","pos":"KeyD","evento":"keydown","campo":"txtNom","ts":"2023-11-04 20:03:13:000090","epoch":1699138993090},"60":{"tecla":"w","pos":"KeyW","evento":"keydown","campo":"txtNom","ts":"2023-11-04 20:03:13:000170","epoch":1699138993170},"61":{"tecla":"a","pos":"KeyA","evento":"keydown","campo":"txtNom","ts":"2023-11-04 20:03:13:000203","epoch":1699138993203},"62":{"tecla":"d","pos":"KeyD","evento":"keyup","campo":"txtNom","ts":"2023-11-04 20:03:13:000226","epoch":1699138993226},"63":{"tecla":"w","pos":"KeyW","evento":"keyup","campo":"txtNom","ts":"2023-11-04 20:03:13:000274","epoch":1699138993274},"64":{"tecla":"a","pos":"KeyA","evento":"keyup","campo":"txtNom","ts":"2023-11-04 20:03:13:000274","epoch":1699138993274}}');
    $mou = json_decode('{"1":{"event_m":"mousemove","coord":"(607, 1254)","ts_m":"2023-11-04 20:07:46:000557","epoch_m":1699139266557},"2":{"event_m":"mousemove","coord":"(601, 1251)","ts_m":"2023-11-04 20:07:46:000557","epoch_m":1699139266558},"3":{"event_m":"mousemove","coord":"(596, 1248)","ts_m":"2023-11-04 20:07:46:000566","epoch_m":1699139266566},"4":{"event_m":"mousemove","coord":"(583, 1241)","ts_m":"2023-11-04 20:07:46:000584","epoch_m":1699139266584},"5":{"event_m":"mousemove","coord":"(476, 1184)","ts_m":"2023-11-04 20:07:46:000729","epoch_m":1699139266729},"6":{"event_m":"mousemove","coord":"(475, 1183)","ts_m":"2023-11-04 20:07:46:000735","epoch_m":1699139266735},"7":{"event_m":"mousemove","coord":"(472, 1182)","ts_m":"2023-11-04 20:07:46:000740","epoch_m":1699139266740},"8":{"event_m":"mousemove","coord":"(470, 1179)","ts_m":"2023-11-04 20:07:46:000748","epoch_m":1699139266748},"9":{"event_m":"mousemove","coord":"(468, 1177)","ts_m":"2023-11-04 20:07:46:000761","epoch_m":1699139266761},"10":{"event_m":"mousemove","coord":"(465, 1175)","ts_m":"2023-11-04 20:07:46:000765","epoch_m":1699139266765},"11":{"event_m":"mousemove","coord":"(463, 1174)","ts_m":"2023-11-04 20:07:46:000772","epoch_m":1699139266772},"12":{"event_m":"mousemove","coord":"(461, 1172)","ts_m":"2023-11-04 20:07:46:000780","epoch_m":1699139266780},"13":{"event_m":"mousemove","coord":"(459, 1169)","ts_m":"2023-11-04 20:07:46:000789","epoch_m":1699139266789},"14":{"event_m":"mousemove","coord":"(458, 1167)","ts_m":"2023-11-04 20:07:46:000796","epoch_m":1699139266796},"15":{"event_m":"mousemove","coord":"(456, 1165)","ts_m":"2023-11-04 20:07:46:000805","epoch_m":1699139266805},"16":{"event_m":"mousemove","coord":"(455, 1164)","ts_m":"2023-11-04 20:07:46:000812","epoch_m":1699139266812},"17":{"event_m":"mousemove","coord":"(454, 1163)","ts_m":"2023-11-04 20:07:46:000820","epoch_m":1699139266820},"18":{"event_m":"mousemove","coord":"(453, 1161)","ts_m":"2023-11-04 20:07:46:000828","epoch_m":1699139266828},"19":{"event_m":"mousemove","coord":"(452, 1160)","ts_m":"2023-11-04 20:07:46:000844","epoch_m":1699139266844},"20":{"event_m":"mousemove","coord":"(451, 1160)","ts_m":"2023-11-04 20:07:46:000861","epoch_m":1699139266861},"21":{"event_m":"mousedown","coord":"(451, 1160)","ts_m":"2023-11-04 20:07:46:000885","epoch_m":1699139266885},"22":{"event_m":"mouseup","coord":"(451, 1160)","ts_m":"2023-11-04 20:07:46:000980","epoch_m":1699139266980},"23":{"event_m":"mousemove","coord":"(450, 1161)","ts_m":"2023-11-04 20:07:47:000046","epoch_m":1699139267046},"24":{"event_m":"mousemove","coord":"(449, 1164)","ts_m":"2023-11-04 20:07:47:000053","epoch_m":1699139267053},"25":{"event_m":"mousemove","coord":"(449, 1171)","ts_m":"2023-11-04 20:07:47:000060","epoch_m":1699139267060},"26":{"event_m":"mousemove","coord":"(449, 1178)","ts_m":"2023-11-04 20:07:47:000068","epoch_m":1699139267068},"27":{"event_m":"mousemove","coord":"(449, 1184)","ts_m":"2023-11-04 20:07:47:000076","epoch_m":1699139267077},"28":{"event_m":"mousemove","coord":"(449, 1192)","ts_m":"2023-11-04 20:07:47:000084","epoch_m":1699139267084},"29":{"event_m":"mousemove","coord":"(449, 1198)","ts_m":"2023-11-04 20:07:47:000092","epoch_m":1699139267092},"30":{"event_m":"mousemove","coord":"(449, 1203)","ts_m":"2023-11-04 20:07:47:000100","epoch_m":1699139267100},"31":{"event_m":"mousemove","coord":"(449, 1210)","ts_m":"2023-11-04 20:07:47:000108","epoch_m":1699139267108},"32":{"event_m":"mousemove","coord":"(449, 1215)","ts_m":"2023-11-04 20:07:47:000116","epoch_m":1699139267116},"33":{"event_m":"mousemove","coord":"(449, 1220)","ts_m":"2023-11-04 20:07:47:000125","epoch_m":1699139267125},"34":{"event_m":"mousemove","coord":"(449, 1222)","ts_m":"2023-11-04 20:07:47:000133","epoch_m":1699139267133},"35":{"event_m":"mousemove","coord":"(449, 1223)","ts_m":"2023-11-04 20:07:47:000140","epoch_m":1699139267140},"36":{"event_m":"mousemove","coord":"(449, 1224)","ts_m":"2023-11-04 20:07:47:000148","epoch_m":1699139267148},"37":{"event_m":"mousemove","coord":"(449, 1225)","ts_m":"2023-11-04 20:07:47:000156","epoch_m":1699139267156},"38":{"event_m":"mousemove","coord":"(450, 1226)","ts_m":"2023-11-04 20:07:47:000236","epoch_m":1699139267236},"39":{"event_m":"mousemove","coord":"(452, 1227)","ts_m":"2023-11-04 20:07:47:000244","epoch_m":1699139267244},"40":{"event_m":"mousemove","coord":"(455, 1228)","ts_m":"2023-11-04 20:07:47:000252","epoch_m":1699139267252},"41":{"event_m":"mousemove","coord":"(456, 1229)","ts_m":"2023-11-04 20:07:47:000260","epoch_m":1699139267260},"42":{"event_m":"mousemove","coord":"(458, 1230)","ts_m":"2023-11-04 20:07:47:000268","epoch_m":1699139267268},"43":{"event_m":"mousemove","coord":"(460, 1231)","ts_m":"2023-11-04 20:07:47:000276","epoch_m":1699139267276},"44":{"event_m":"mousemove","coord":"(463, 1232)","ts_m":"2023-11-04 20:07:47:000284","epoch_m":1699139267284},"45":{"event_m":"mousemove","coord":"(464, 1233)","ts_m":"2023-11-04 20:07:47:000293","epoch_m":1699139267293},"46":{"event_m":"mousemove","coord":"(465, 1233)","ts_m":"2023-11-04 20:07:47:000300","epoch_m":1699139267300},"47":{"event_m":"mousemove","coord":"(467, 1234)","ts_m":"2023-11-04 20:07:47:000308","epoch_m":1699139267308},"48":{"event_m":"mousemove","coord":"(469, 1235)","ts_m":"2023-11-04 20:07:47:000316","epoch_m":1699139267316},"49":{"event_m":"mousemove","coord":"(470, 1235)","ts_m":"2023-11-04 20:07:47:000324","epoch_m":1699139267324},"50":{"event_m":"mousemove","coord":"(472, 1236)","ts_m":"2023-11-04 20:07:47:000333","epoch_m":1699139267333},"51":{"event_m":"mousemove","coord":"(473, 1236)","ts_m":"2023-11-04 20:07:47:000349","epoch_m":1699139267349},"52":{"event_m":"mousemove","coord":"(473, 1237)","ts_m":"2023-11-04 20:07:47:000357","epoch_m":1699139267357},"53":{"event_m":"mousedown","coord":"(473, 1237)","ts_m":"2023-11-04 20:07:47:000357","epoch_m":1699139267357},"54":{"event_m":"mouseup","coord":"(473, 1237)","ts_m":"2023-11-04 20:07:47:000437","epoch_m":1699139267437},"55":{"event_m":"mousemove","coord":"(472, 1237)","ts_m":"2023-11-04 20:07:47:000445","epoch_m":1699139267445},"56":{"event_m":"mousemove","coord":"(468, 1237)","ts_m":"2023-11-04 20:07:47:000453","epoch_m":1699139267453},"57":{"event_m":"mousemove","coord":"(461, 1237)","ts_m":"2023-11-04 20:07:47:000460","epoch_m":1699139267460},"58":{"event_m":"mousemove","coord":"(452, 1237)","ts_m":"2023-11-04 20:07:47:000469","epoch_m":1699139267469},"59":{"event_m":"mousemove","coord":"(441, 1238)","ts_m":"2023-11-04 20:07:47:000476","epoch_m":1699139267476},"60":{"event_m":"mousemove","coord":"(428, 1239)","ts_m":"2023-11-04 20:07:47:000485","epoch_m":1699139267485},"61":{"event_m":"mousemove","coord":"(414, 1239)","ts_m":"2023-11-04 20:07:47:000492","epoch_m":1699139267492},"62":{"event_m":"mousemove","coord":"(404, 1239)","ts_m":"2023-11-04 20:07:47:000501","epoch_m":1699139267501},"63":{"event_m":"mousemove","coord":"(396, 1239)","ts_m":"2023-11-04 20:07:47:000508","epoch_m":1699139267508},"64":{"event_m":"mousemove","coord":"(390, 1239)","ts_m":"2023-11-04 20:07:47:000517","epoch_m":1699139267517},"65":{"event_m":"mousemove","coord":"(388, 1239)","ts_m":"2023-11-04 20:07:47:000524","epoch_m":1699139267524},"66":{"event_m":"mousemove","coord":"(387, 1239)","ts_m":"2023-11-04 20:07:47:000541","epoch_m":1699139267541},"67":{"event_m":"mousedown","coord":"(387, 1239)","ts_m":"2023-11-04 20:07:47:000637","epoch_m":1699139267637},"68":{"event_m":"mousemove","coord":"(387, 1239)","ts_m":"2023-11-04 20:07:47:000668","epoch_m":1699139267668},"69":{"event_m":"mouseup","coord":"(387, 1239)","ts_m":"2023-11-04 20:07:47:000733","epoch_m":1699139267733},"70":{"event_m":"mousemove","coord":"(385, 1239)","ts_m":"2023-11-04 20:07:47:000806","epoch_m":1699139267806},"71":{"event_m":"mousemove","coord":"(384, 1239)","ts_m":"2023-11-04 20:07:47:000814","epoch_m":1699139267814},"72":{"event_m":"mousemove","coord":"(381, 1239)","ts_m":"2023-11-04 20:07:47:000821","epoch_m":1699139267821},"73":{"event_m":"mousemove","coord":"(378, 1239)","ts_m":"2023-11-04 20:07:47:000829","epoch_m":1699139267829},"74":{"event_m":"mousemove","coord":"(376, 1239)","ts_m":"2023-11-04 20:07:47:000837","epoch_m":1699139267837},"75":{"event_m":"mousemove","coord":"(372, 1239)","ts_m":"2023-11-04 20:07:47:000844","epoch_m":1699139267844},"76":{"event_m":"mousemove","coord":"(369, 1239)","ts_m":"2023-11-04 20:07:47:000853","epoch_m":1699139267853},"77":{"event_m":"mousemove","coord":"(366, 1239)","ts_m":"2023-11-04 20:07:47:000860","epoch_m":1699139267860},"78":{"event_m":"mousemove","coord":"(362, 1239)","ts_m":"2023-11-04 20:07:47:000869","epoch_m":1699139267869},"79":{"event_m":"mousemove","coord":"(359, 1239)","ts_m":"2023-11-04 20:07:47:000877","epoch_m":1699139267877},"80":{"event_m":"mousemove","coord":"(356, 1239)","ts_m":"2023-11-04 20:07:47:000885","epoch_m":1699139267885},"81":{"event_m":"mousemove","coord":"(353, 1239)","ts_m":"2023-11-04 20:07:47:000893","epoch_m":1699139267893},"82":{"event_m":"mousemove","coord":"(351, 1239)","ts_m":"2023-11-04 20:07:47:000901","epoch_m":1699139267901},"83":{"event_m":"mousemove","coord":"(349, 1239)","ts_m":"2023-11-04 20:07:47:000909","epoch_m":1699139267909},"84":{"event_m":"mousemove","coord":"(347, 1239)","ts_m":"2023-11-04 20:07:47:000918","epoch_m":1699139267918},"85":{"event_m":"mousemove","coord":"(346, 1239)","ts_m":"2023-11-04 20:07:47:000934","epoch_m":1699139267934},"86":{"event_m":"mousemove","coord":"(345, 1239)","ts_m":"2023-11-04 20:07:48:000077","epoch_m":1699139268077},"87":{"event_m":"mousemove","coord":"(345, 1240)","ts_m":"2023-11-04 20:07:48:000085","epoch_m":1699139268085},"88":{"event_m":"mousemove","coord":"(344, 1240)","ts_m":"2023-11-04 20:07:48:000093","epoch_m":1699139268093},"89":{"event_m":"mousemove","coord":"(343, 1240)","ts_m":"2023-11-04 20:07:48:000101","epoch_m":1699139268101},"90":{"event_m":"mousemove","coord":"(342, 1241)","ts_m":"2023-11-04 20:07:48:000109","epoch_m":1699139268109},"91":{"event_m":"mousemove","coord":"(342, 1242)","ts_m":"2023-11-04 20:07:48:000118","epoch_m":1699139268118},"92":{"event_m":"mousemove","coord":"(340, 1242)","ts_m":"2023-11-04 20:07:48:000125","epoch_m":1699139268125},"93":{"event_m":"mousemove","coord":"(339, 1243)","ts_m":"2023-11-04 20:07:48:000133","epoch_m":1699139268133},"94":{"event_m":"mousedown","coord":"(339, 1243)","ts_m":"2023-11-04 20:07:48:000189","epoch_m":1699139268189},"95":{"event_m":"mouseup","coord":"(339, 1243)","ts_m":"2023-11-04 20:07:48:000293","epoch_m":1699139268293},"96":{"event_m":"mousemove","coord":"(339, 1244)","ts_m":"2023-11-04 20:07:48:000317","epoch_m":1699139268317},"97":{"event_m":"mousemove","coord":"(339, 1245)","ts_m":"2023-11-04 20:07:48:000325","epoch_m":1699139268325},"98":{"event_m":"mousemove","coord":"(339, 1247)","ts_m":"2023-11-04 20:07:48:000333","epoch_m":1699139268333},"99":{"event_m":"mousemove","coord":"(339, 1251)","ts_m":"2023-11-04 20:07:48:000340","epoch_m":1699139268340},"100":{"event_m":"mousemove","coord":"(339, 1256)","ts_m":"2023-11-04 20:07:48:000349","epoch_m":1699139268349},"101":{"event_m":"mousemove","coord":"(339, 1262)","ts_m":"2023-11-04 20:07:48:000357","epoch_m":1699139268357},"102":{"event_m":"mousemove","coord":"(341, 1269)","ts_m":"2023-11-04 20:07:48:000365","epoch_m":1699139268365},"103":{"event_m":"mousemove","coord":"(343, 1276)","ts_m":"2023-11-04 20:07:48:000373","epoch_m":1699139268373},"104":{"event_m":"mousemove","coord":"(345, 1282)","ts_m":"2023-11-04 20:07:48:000381","epoch_m":1699139268381},"105":{"event_m":"mousemove","coord":"(348, 1289)","ts_m":"2023-11-04 20:07:48:000389","epoch_m":1699139268389},"106":{"event_m":"mousemove","coord":"(351, 1296)","ts_m":"2023-11-04 20:07:48:000397","epoch_m":1699139268397},"107":{"event_m":"mousemove","coord":"(354, 1303)","ts_m":"2023-11-04 20:07:48:000405","epoch_m":1699139268405},"108":{"event_m":"mousemove","coord":"(358, 1310)","ts_m":"2023-11-04 20:07:48:000412","epoch_m":1699139268413},"109":{"event_m":"mousemove","coord":"(361, 1318)","ts_m":"2023-11-04 20:07:48:000421","epoch_m":1699139268421},"110":{"event_m":"mousemove","coord":"(364, 1325)","ts_m":"2023-11-04 20:07:48:000429","epoch_m":1699139268429},"111":{"event_m":"mousemove","coord":"(368, 1331)","ts_m":"2023-11-04 20:07:48:000437","epoch_m":1699139268437},"112":{"event_m":"mousemove","coord":"(371, 1335)","ts_m":"2023-11-04 20:07:48:000445","epoch_m":1699139268445},"113":{"event_m":"mousemove","coord":"(373, 1338)","ts_m":"2023-11-04 20:07:48:000453","epoch_m":1699139268453},"114":{"event_m":"mousemove","coord":"(374, 1339)","ts_m":"2023-11-04 20:07:48:000461","epoch_m":1699139268461},"115":{"event_m":"mousemove","coord":"(375, 1340)","ts_m":"2023-11-04 20:07:48:000469","epoch_m":1699139268469},"116":{"event_m":"mousedown","coord":"(375, 1340)","ts_m":"2023-11-04 20:07:48:000557","epoch_m":1699139268557},"117":{"event_m":"mousemove","coord":"(375, 1340)","ts_m":"2023-11-04 20:07:48:000587","epoch_m":1699139268587},"118":{"event_m":"mousemove","coord":"(375, 1340)","ts_m":"2023-11-04 20:07:48:000601","epoch_m":1699139268601},"119":{"event_m":"mouseup","coord":"(375, 1340)","ts_m":"2023-11-04 20:07:48:000653","epoch_m":1699139268653},"120":{"event_m":"mousemove","coord":"(375, 1342)","ts_m":"2023-11-04 20:07:48:000735","epoch_m":1699139268735},"121":{"event_m":"mousemove","coord":"(377, 1345)","ts_m":"2023-11-04 20:07:48:000742","epoch_m":1699139268742},"122":{"event_m":"mousemove","coord":"(380, 1351)","ts_m":"2023-11-04 20:07:48:000749","epoch_m":1699139268749},"123":{"event_m":"mousemove","coord":"(401, 1411)","ts_m":"2023-11-04 20:07:48:000814","epoch_m":1699139268814},"124":{"event_m":"mousemove","coord":"(403, 1420)","ts_m":"2023-11-04 20:07:48:000821","epoch_m":1699139268821},"125":{"event_m":"mousemove","coord":"(404, 1430)","ts_m":"2023-11-04 20:07:48:000829","epoch_m":1699139268829},"126":{"event_m":"mousemove","coord":"(405, 1439)","ts_m":"2023-11-04 20:07:48:000837","epoch_m":1699139268837},"127":{"event_m":"mousemove","coord":"(408, 1449)","ts_m":"2023-11-04 20:07:48:000846","epoch_m":1699139268846},"128":{"event_m":"mousemove","coord":"(410, 1458)","ts_m":"2023-11-04 20:07:48:000853","epoch_m":1699139268853},"129":{"event_m":"mousemove","coord":"(411, 1468)","ts_m":"2023-11-04 20:07:48:000861","epoch_m":1699139268861},"130":{"event_m":"mousemove","coord":"(412, 1475)","ts_m":"2023-11-04 20:07:48:000869","epoch_m":1699139268869},"131":{"event_m":"mousemove","coord":"(413, 1479)","ts_m":"2023-11-04 20:07:48:000878","epoch_m":1699139268878},"132":{"event_m":"mousemove","coord":"(413, 1482)","ts_m":"2023-11-04 20:07:48:000886","epoch_m":1699139268886},"133":{"event_m":"mousemove","coord":"(413, 1483)","ts_m":"2023-11-04 20:07:48:000893","epoch_m":1699139268893},"134":{"event_m":"mousemove","coord":"(413, 1484)","ts_m":"2023-11-04 20:07:48:000901","epoch_m":1699139268901},"135":{"event_m":"mousedown","coord":"(413, 1484)","ts_m":"2023-11-04 20:07:49:000261","epoch_m":1699139269261},"136":{"event_m":"mouseup","coord":"(413, 1484)","ts_m":"2023-11-04 20:07:49:000333","epoch_m":1699139269333}}');
    $comp = json_decode('{"1":{"ord":["txtNum","txtAno","txtMes","txtCVC","txtNom"],"num_type":"Digit","up_type":"None","time_txt":{"txtNum":{"Started":{"Timestamp":"2023-11-04 20:08:45:000057","Epoch":1699139325057},"Finished":{"Timestamp":"2023-11-04 20:08:45:000720","Epoch":1699139325720}},"txtNom":{"Started":{"Timestamp":"2023-11-04 20:08:47:000495","Epoch":1699139327495},"Finished":{"Timestamp":"2023-11-04 20:08:48:000128","Epoch":1699139328128}},"txtMes":{"Started":{"Timestamp":"2023-11-04 20:08:46:000272","Epoch":1699139326272},"Finished":{"Timestamp":"2023-11-04 20:08:46:000712","Epoch":1699139326712}},"txtAno":{"Started":{"Timestamp":"2023-11-04 20:08:45:000720","Epoch":1699139325720},"Finished":{"Timestamp":"2023-11-04 20:08:46:000272","Epoch":1699139326272}},"txtCVC":{"Started":{"Timestamp":"2023-11-04 20:08:46:000712","Epoch":1699139326712},"Finished":{"Timestamp":"2023-11-04 20:08:47:000200","Epoch":1699139327200}}},"time_form":{"Started":{"Timestamp":"2023-11-04 20:08:45:000057","Epoch":1699139325057},"Finished":{"Timestamp":"2023-11-04 20:08:48:000128","Epoch":1699139328128}}}}');

    // echo($dig);
    // echo($mou);
    echo(var_dump($comp));

    // $comando = 'insert into t values("'.$mou.'")';

    // mysqli_query($link,$comando);
?>