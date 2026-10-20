# EMA Hourly Continuation — REQ/USDT P12_50

**Symbol:** REQ/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1161 |
| net_profit_factor | 0.4135 |
| net_win_rate | 0.4065 |
| gross_profit_factor | 0.8234 |
| gross_win_rate | 0.4376 |
| sharpe_ratio | -10.6133 |
| sortino_ratio | -5.1108 |
| max_drawdown | 0.9986 |
| cagr | -0.9259 |
| net_avg_win | 14.9142 |
| net_avg_loss | -24.7097 |
| avg_hold_time_bars | 6.9707 |
| exposure | 0.3679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
