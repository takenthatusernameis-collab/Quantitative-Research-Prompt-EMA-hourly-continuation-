# EMA Hourly Continuation — XDC/USDT P89_100

**Symbol:** XDC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.0735 |
| net_win_rate | 0.2864 |
| gross_profit_factor | 0.4143 |
| gross_win_rate | 0.3798 |
| sharpe_ratio | -13.2577 |
| sortino_ratio | -5.2667 |
| max_drawdown | 0.9995 |
| cagr | -0.9509 |
| net_avg_win | 4.1100 |
| net_avg_loss | -22.4284 |
| avg_hold_time_bars | 2.3042 |
| exposure | 0.0706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
