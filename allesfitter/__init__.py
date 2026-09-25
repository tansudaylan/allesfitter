#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:18:20 2018

@author:
Maximilian N. Günther
MIT Kavli Institute for Astrophysics and Space Research, 
Massachusetts Institute of Technology,
77 Massachusetts Avenue,
Cambridge, MA 02109, 
USA
Email: maxgue@mit.edu
Web: www.mnguenther.com
"""

from __future__ import print_function, division, absolute_import

from importlib import import_module
import os


_LAZY_EXPORTS = {
    'generate_phase_folded_figure': ('.diagnostics', 'generate_phase_folded_figure'),
    'load_light_curve': ('.diagnostics', 'load_light_curve'),
    'mcmc_fit': ('.mcmc', 'mcmc_fit'),
    'ns_fit': ('.nested_sampling', 'ns_fit'),
    'get_labels': ('.general_output', 'get_labels'),
    'get_ns_posterior_samples': ('.nested_sampling_output', 'get_ns_posterior_samples'),
    'ns_output': ('.nested_sampling_output', 'ns_output'),
    'get_mcmc_posterior_samples': ('.mcmc_output', 'get_mcmc_posterior_samples'),
    'mcmc_output': ('.mcmc_output', 'mcmc_output'),
    'transform_priors': ('.priors', 'transform_priors'),
    'estimate_noise': ('.priors.estimate_noise', 'estimate_noise'),
    'ns_plot_bayes_factors': ('.postprocessing.nested_sampling_compare_logZ', 'ns_plot_bayes_factors'),
    'ns_plot_violins': ('.postprocessing.plot_violins', 'ns_plot_violins'),
    'mcmc_plot_violins': ('.postprocessing.plot_violins', 'mcmc_plot_violins'),
}


def __getattr__(name):
    """Load optional fitting and postprocessing dependencies on first use."""

    if name not in _LAZY_EXPORTS:
        raise AttributeError("module 'allesfitter' has no attribute %r" % name)
    module_name, attribute_name = _LAZY_EXPORTS[name]
    value = getattr(import_module(module_name, __name__), attribute_name)
    globals()[name] = value
    return value

def GUI():
    allesfitter_path = os.path.dirname( os.path.realpath(__file__) )
    os.system( 'jupyter notebook "' + os.path.join(allesfitter_path,'GUI.ipynb') + '"')

#::: version
__version__ = '0.8.0'
