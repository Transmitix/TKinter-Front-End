#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: Nilakna
# GNU Radio version: v3.11.0.0git-848-g6fd69852

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import fec
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import soapy
import nack1_epy_block_1_0 as epy_block_1_0  # embedded python block
import sip
import threading



class nack1(gr.top_block, Qt.QWidget):

    def __init__(self, MTU=1500):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "nack1")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Parameters
        ##################################################
        self.MTU = MTU

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.qpsk = qpsk = digital.constellation_rect([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j], [0, 1, 2, 3],
        4, 2, 2, 1, 1).base()
        self.polys = polys = [109, 79]
        self.nfilts = nfilts = 32
        self.k = k = 7
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0 = digital.adaptive_algorithm_cma( qpsk, .0001, 4).base()
        self.tx_freq = tx_freq = 600e6
        self.timing_loop_bw = timing_loop_bw = 6.28/100.0
        self.time_offset = time_offset = 1.00
        self.taps = taps = [1.0, 0.25-0.25j, 0.50 + 0.10j, -0.3 + 0.2j]
        self.spr = spr = 100000
        self.samp_rate_blade = samp_rate_blade = 750e3
        self.samp_rate_0 = samp_rate_0 = 750e3
        self.samp_rate = samp_rate = 32000
        self.rx_freq_ = rx_freq_ = 433e6
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.rf_gain_sink = rf_gain_sink = 10
        self.rf_gain_0 = rf_gain_0 = 60
        self.rf_gain = rf_gain = 60
        self.phase_bw = phase_bw = 6.28/100.0
        self.noise_volt = noise_volt = 0.0001
        self.if_gain = if_gain = 40
        self.hdr_format = hdr_format = digital.header_format_default('00011010110011111111110000011101',1, 1)
        self.freq_offset = freq_offset = 0
        self.freq = freq = 2.4e9
        self.excess_bw = excess_bw = .5
        self.eq_gain = eq_gain = 0.01
        self.delay = delay = 42
        self.cc_enc = cc_enc = fec.cc_encoder_make((MTU*8),k, 2, polys, 0, fec.CC_TAILBITING, True)
        self.cc_dec = cc_dec = list(map( (lambda a: fec.cc_decoder.make((MTU*8),k, 2, polys, 0, (-1), fec.CC_TAILBITING, True)),range(0,1)))
        self.bw = bw = 10e3
        self.arity = arity = 4

        ##################################################
        # Blocks
        ##################################################

        self._freq_range = qtgui.Range(2e9, 6e9, 100e3, 2.4e9, 200)
        self._freq_win = qtgui.RangeWidget(self._freq_range, self.set_freq, "'freq'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._freq_win)
        self.controls = Qt.QTabWidget()
        self.controls_widget_0 = Qt.QWidget()
        self.controls_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_0)
        self.controls_grid_layout_0 = Qt.QGridLayout()
        self.controls_layout_0.addLayout(self.controls_grid_layout_0)
        self.controls.addTab(self.controls_widget_0, 'Channel')
        self.controls_widget_1 = Qt.QWidget()
        self.controls_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_1)
        self.controls_grid_layout_1 = Qt.QGridLayout()
        self.controls_layout_1.addLayout(self.controls_grid_layout_1)
        self.controls.addTab(self.controls_widget_1, 'Receiver')
        self.top_grid_layout.addWidget(self.controls, 0, 0, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._timing_loop_bw_range = qtgui.Range(0.0, 0.2, 0.01, 6.28/100.0, 200)
        self._timing_loop_bw_win = qtgui.RangeWidget(self._timing_loop_bw_range, self.set_timing_loop_bw, "Time: BW", "slider", float, QtCore.Qt.Horizontal)
        self.controls_grid_layout_1.addWidget(self._timing_loop_bw_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.controls_grid_layout_1.setColumnStretch(c, 1)
        self._time_offset_range = qtgui.Range(0.999, 1.001, 0.0001, 1.00, 200)
        self._time_offset_win = qtgui.RangeWidget(self._time_offset_range, self.set_time_offset, "Timing Offset", "counter_slider", float, QtCore.Qt.Horizontal)
        self.controls_grid_layout_0.addWidget(self._time_offset_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 3):
            self.controls_grid_layout_0.setColumnStretch(c, 1)
        self.soapy_bladerf_sink_0 = None
        dev = 'driver=bladerf'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_bladerf_sink_0 = soapy.sink(dev, "fc32", 1, 'bladerf=0',
                                  stream_args, tune_args, settings)
        self.soapy_bladerf_sink_0.set_sample_rate(0, 1200000)
        self.soapy_bladerf_sink_0.set_bandwidth(0, 9000)
        self.soapy_bladerf_sink_0.set_frequency(0, freq)
        self.soapy_bladerf_sink_0.set_frequency_correction(0, 0)
        self.soapy_bladerf_sink_0.set_gain(0, min(max(60, 17.0), 73.0))
        self._rf_gain_sink_range = qtgui.Range(0, 60, 1, 10, 200)
        self._rf_gain_sink_win = qtgui.RangeWidget(self._rf_gain_sink_range, self.set_rf_gain_sink, "RF gain sink", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._rf_gain_sink_win)
        self._rf_gain_0_range = qtgui.Range(0, 60, 1, 60, 200)
        self._rf_gain_0_win = qtgui.RangeWidget(self._rf_gain_0_range, self.set_rf_gain_0, "RF gain", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._rf_gain_0_win)
        self._rf_gain_range = qtgui.Range(0, 60, 1, 60, 200)
        self._rf_gain_win = qtgui.RangeWidget(self._rf_gain_range, self.set_rf_gain, "RF gain", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._rf_gain_win)
        self.received = Qt.QTabWidget()
        self.received_widget_0 = Qt.QWidget()
        self.received_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.received_widget_0)
        self.received_grid_layout_0 = Qt.QGridLayout()
        self.received_layout_0.addLayout(self.received_grid_layout_0)
        self.received.addTab(self.received_widget_0, 'Constellation')
        self.received_widget_1 = Qt.QWidget()
        self.received_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.received_widget_1)
        self.received_grid_layout_1 = Qt.QGridLayout()
        self.received_layout_1.addLayout(self.received_grid_layout_1)
        self.received.addTab(self.received_widget_1, 'Symbols')
        self.top_grid_layout.addWidget(self.received, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            'Before RRC', #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self._phase_bw_range = qtgui.Range(0.0, 1.0, 0.01, 6.28/100.0, 200)
        self._phase_bw_win = qtgui.RangeWidget(self._phase_bw_range, self.set_phase_bw, "Phase: Bandwidth", "slider", float, QtCore.Qt.Horizontal)
        self.controls_grid_layout_1.addWidget(self._phase_bw_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_1.setRowStretch(r, 1)
        for c in range(2, 3):
            self.controls_grid_layout_1.setColumnStretch(c, 1)
        self._noise_volt_range = qtgui.Range(0, 1, 0.01, 0.0001, 200)
        self._noise_volt_win = qtgui.RangeWidget(self._noise_volt_range, self.set_noise_volt, "Noise Voltage", "counter_slider", float, QtCore.Qt.Horizontal)
        self.controls_grid_layout_0.addWidget(self._noise_volt_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.controls_grid_layout_0.setColumnStretch(c, 1)
        self._if_gain_range = qtgui.Range(0, 50, 1, 40, 200)
        self._if_gain_win = qtgui.RangeWidget(self._if_gain_range, self.set_if_gain, "IF gain", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._if_gain_win)
        self._freq_offset_range = qtgui.Range(-0.1, 0.1, 0.001, 0, 200)
        self._freq_offset_win = qtgui.RangeWidget(self._freq_offset_range, self.set_freq_offset, "Frequency Offset", "counter_slider", float, QtCore.Qt.Horizontal)
        self.controls_grid_layout_0.addWidget(self._freq_offset_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.controls_grid_layout_0.setColumnStretch(c, 1)
        self.fec_extended_tagged_encoder_0_1 = fec.extended_tagged_encoder(encoder_obj_list=cc_enc, puncpat='11', lentagname="packet_len", mtu=MTU)
        self._eq_gain_range = qtgui.Range(0.0, 0.1, 0.001, 0.01, 200)
        self._eq_gain_win = qtgui.RangeWidget(self._eq_gain_range, self.set_eq_gain, "Equalizer: rate", "slider", float, QtCore.Qt.Horizontal)
        self.controls_grid_layout_1.addWidget(self._eq_gain_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.controls_grid_layout_1.setColumnStretch(c, 1)
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(hdr_format, "packet_len")
        self.digital_constellation_modulator_0 = digital.generic_mod(
            constellation=qpsk,
            differential=True,
            samples_per_symbol=sps,
            pre_diff_code=True,
            excess_bw=excess_bw,
            verbose=False,
            log=False,
            truncate=False)
        self._delay_range = qtgui.Range(0, 200, 1, 42, 200)
        self._delay_win = qtgui.RangeWidget(self._delay_range, self.set_delay, "Delay", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._delay_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, "packet_len", 0)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 16, "packet_len")
        self.blocks_repack_bits_bb_0_0_0 = blocks.repack_bits_bb(1, 8, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, 1, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(0.8)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/thevinduk/Repositories/TKinter-Front-End/Chats/Sent/message.txt', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.soapy_bladerf_sink_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.fec_extended_tagged_encoder_0_1, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.digital_protocol_formatter_bb_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0_1, 0), (self.blocks_repack_bits_bb_0_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "nack1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_MTU(self):
        return self.MTU

    def set_MTU(self, MTU):
        self.MTU = MTU

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_variable_adaptive_algorithm_0(self):
        return self.variable_adaptive_algorithm_0

    def set_variable_adaptive_algorithm_0(self, variable_adaptive_algorithm_0):
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0

    def get_tx_freq(self):
        return self.tx_freq

    def set_tx_freq(self, tx_freq):
        self.tx_freq = tx_freq

    def get_timing_loop_bw(self):
        return self.timing_loop_bw

    def set_timing_loop_bw(self, timing_loop_bw):
        self.timing_loop_bw = timing_loop_bw

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps

    def get_spr(self):
        return self.spr

    def set_spr(self, spr):
        self.spr = spr
        self.blocks_throttle2_0_0.set_sample_rate(self.spr)

    def get_samp_rate_blade(self):
        return self.samp_rate_blade

    def set_samp_rate_blade(self, samp_rate_blade):
        self.samp_rate_blade = samp_rate_blade

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_1.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, 187500, 0.2, 64))

    def get_rx_freq_(self):
        return self.rx_freq_

    def set_rx_freq_(self, rx_freq_):
        self.rx_freq_ = rx_freq_

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_rf_gain_sink(self):
        return self.rf_gain_sink

    def set_rf_gain_sink(self, rf_gain_sink):
        self.rf_gain_sink = rf_gain_sink

    def get_rf_gain_0(self):
        return self.rf_gain_0

    def set_rf_gain_0(self, rf_gain_0):
        self.rf_gain_0 = rf_gain_0

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format
        self.digital_protocol_formatter_bb_0.set_header_format(self.hdr_format)

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.soapy_bladerf_sink_0.set_frequency(0, self.freq)

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_eq_gain(self):
        return self.eq_gain

    def set_eq_gain(self, eq_gain):
        self.eq_gain = eq_gain

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay

    def get_cc_enc(self):
        return self.cc_enc

    def set_cc_enc(self, cc_enc):
        self.cc_enc = cc_enc

    def get_cc_dec(self):
        return self.cc_dec

    def set_cc_dec(self, cc_dec):
        self.cc_dec = cc_dec

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--MTU", dest="MTU", type=intx, default=1500,
        help="Set MTU [default=%(default)r]")
    return parser


def main(top_block_cls=nack1, options=None):
    if options is None:
        options = argument_parser().parse_args()

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(MTU=options.MTU)

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
