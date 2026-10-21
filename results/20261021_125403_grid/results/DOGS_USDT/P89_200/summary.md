# EMA Hourly Continuation — DOGS/USDT P89_200

**Symbol:** DOGS/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.7825 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9545 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -1.2459 |
| sortino_ratio | -0.2980 |
| max_drawdown | 0.3081 |
| cagr | -0.1289 |
| net_avg_win | 78.3050 |
| net_avg_loss | -96.7890 |
| avg_hold_time_bars | 14.3917 |
| exposure | 0.1832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
