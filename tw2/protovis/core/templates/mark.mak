${w.parent_js_id}.add(${w.pvcls.src})
% for f in w._pv_prop_funcs:
	${f.src}
% endfor
% for a in w._adds:
${a.display()}

% endfor
