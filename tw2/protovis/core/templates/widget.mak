<%namespace name="tw" module="tw2.core.mako_util"/>
<div ${tw.attrs(attrs=w.attrs)}>
<script type="text/javascript+protovis">
${w.init_js.src|n}
var vis = new pv.Panel()
% for f in w._pv_prop_funcs:
	${f.src|n}
% endfor

% for a in w._adds:
${a.display()|n}

% endfor
vis.render();

</script>
</div>
