#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Jan 31 03:47:33 2022
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import lora
import osmosdr
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.GetWin(),
        	baseband_freq=868e6,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=1e6,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Waterfall Plot',
        )
        self.Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=868e6,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=1e6,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(1e6)
        self.osmosdr_source_0.set_center_freq(868e6, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('TX/RX', 0)
        self.osmosdr_source_0.set_bandwidth(1e6, 0)

        self.lora_lora_receiver_1_2_0_0 = lora.lora_receiver(1e6, 868e6, ([868.5e6]), 125000, 10, False, 4, True, False, False, 1, False, False)
        self.lora_lora_receiver_1_2_0 = lora.lora_receiver(1e6, 868e6, ([868.5e6]), 125000, 8, False, 4, True, False, False, 1, False, False)
        self.lora_lora_receiver_1_2 = lora.lora_receiver(1e6, 868e6, ([868.5e6]), 125000, 12, False, 4, True, False, False, 1, False, False)
        self.lora_lora_receiver_1_1 = lora.lora_receiver(1e6, 868e6, ([868.5e6]), 125000, 9, False, 4, True, False, False, 1, False, False)
        self.lora_lora_receiver_1_0_1_0_0 = lora.lora_receiver(1e6, 868e6, ([868.3e6]), 125000, 10, False, 4, True, False, False, 1, False, False)
        self.lora_lora_receiver_1_0_1_0 = lora.lora_receiver(1e6, 868e6, ([868.3e6]), 125000, 8, False, 4, True, False, False, 1, False, False)
        self.lora_lora_receiver_1_0_1 = lora.lora_receiver(1e6, 868e6, ([868.3e6]), 125000, 12, False, 4, True, False, False, 1, False, False)
        self.lora_lora_receiver_1_0_0 = lora.lora_receiver(1e6, 868e6, ([868.3e6]), 125000, 9, False, 4, True, False, False, 1, False, False)
        self.lora_lora_receiver_1_0 = lora.lora_receiver(1e6, 868e6, ([868.3e6]), 125000, 7, False, 4, True, False, False, 1, False, False)
        self.lora_lora_receiver_1 = lora.lora_receiver(1e6, 868e6, ([868.5e6]), 125000, 7, False, 4, True, False, False, 1, False, False)
        self.lora_lora_receiver_0_1_0_0 = lora.lora_receiver(1e6, 868e6, ([868.1e6]), 125000, 10, False, 4, True, False, False, 1, False, False)
        self.lora_lora_receiver_0_1_0 = lora.lora_receiver(1e6, 868e6, ([868.1e6]), 125000, 8, False, 4, True, False, False, 1, False, False)
        self.lora_lora_receiver_0_1 = lora.lora_receiver(1e6, 868e6, ([868.1e6]), 125000, 12, False, 4, True, False, False, 1, False, False)
        self.lora_lora_receiver_0_0 = lora.lora_receiver(1e6, 868e6, ([868.1e6]), 125000, 9, False, 4, True, False, False, 1, False, False)
        self.lora_lora_receiver_0 = lora.lora_receiver(1e6, 868e6, ([868.1e6]), 125000, 7, False, 4, True, False, False, 1, False, False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_0_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_0_1_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_0_1_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_1_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_1_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_1_0_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_1_0_1_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_1_0_1_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_1_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_1_2, 0))
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_1_2_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.lora_lora_receiver_1_2_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_waterfallsink2_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
