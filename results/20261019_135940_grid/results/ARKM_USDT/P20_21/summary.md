# EMA Hourly Continuation — ARKM/USDT P20_21

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1267 |
| net_profit_factor | 0.2083 |
| net_win_rate | 0.3015 |
| gross_profit_factor | 0.6549 |
| gross_win_rate | 0.3694 |
| sharpe_ratio | -17.5865 |
| sortino_ratio | -9.3131 |
| max_drawdown | 1.0000 |
| cagr | -0.9951 |
| net_avg_win | 6.8885 |
| net_avg_loss | -14.2728 |
| avg_hold_time_bars | 1.6212 |
| exposure | 0.0934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
