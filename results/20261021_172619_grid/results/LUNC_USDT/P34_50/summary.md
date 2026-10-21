# EMA Hourly Continuation — LUNC/USDT P34_50

**Symbol:** LUNC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 209 |
| net_profit_factor | 0.6175 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8705 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -2.0272 |
| sortino_ratio | -0.4196 |
| max_drawdown | 0.3973 |
| cagr | -0.1745 |
| net_avg_win | 62.3070 |
| net_avg_loss | -90.8190 |
| avg_hold_time_bars | 5.6890 |
| exposure | 0.0540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
