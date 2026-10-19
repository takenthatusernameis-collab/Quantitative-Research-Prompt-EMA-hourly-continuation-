# EMA Hourly Continuation — FLOKI/USDT P21_50

**Symbol:** FLOKI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1090 |
| net_profit_factor | 0.5171 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8596 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -7.6470 |
| sortino_ratio | -3.5388 |
| max_drawdown | 0.9889 |
| cagr | -0.8279 |
| net_avg_win | 21.5459 |
| net_avg_loss | -34.1546 |
| avg_hold_time_bars | 4.1862 |
| exposure | 0.2074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
