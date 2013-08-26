var ${w.js_id|n};
${w.js_id|n} = ${w.parent_js_id|n}.${w.add_method|n}(${w.pvcls.src|n})
% for f in w._pv_prop_funcs:
	${f.src|n}
% endfor

% for a in w._adds:
${a.display()|n}

% endfor
