var ${w.js_id};
${w.js_id} = ${w.parent_js_id}.${w.add_method}(${w.pvcls.src})
% for f in w._pv_prop_funcs:
	${f.src}
% endfor

% for a in w._adds:
${a.display()}

% endfor
