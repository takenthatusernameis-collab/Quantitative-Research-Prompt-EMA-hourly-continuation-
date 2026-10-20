# EMA Hourly Continuation — MINA/USDT P34_50

**Symbol:** MINA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 920 |
| net_profit_factor | 0.4620 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 1.0176 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -7.5066 |
| sortino_ratio | -3.2164 |
| max_drawdown | 0.9828 |
| cagr | -0.7992 |
| net_avg_win | 19.8041 |
| net_avg_loss | -36.9616 |
| avg_hold_time_bars | 3.0543 |
| exposure | 0.1277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
