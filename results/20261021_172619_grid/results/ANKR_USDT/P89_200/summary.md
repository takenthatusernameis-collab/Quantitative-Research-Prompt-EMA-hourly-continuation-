# EMA Hourly Continuation — ANKR/USDT P89_200

**Symbol:** ANKR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7089 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9567 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -1.9131 |
| sortino_ratio | -0.4817 |
| max_drawdown | 0.4363 |
| cagr | -0.1997 |
| net_avg_win | 68.6452 |
| net_avg_loss | -93.1545 |
| avg_hold_time_bars | 18.6194 |
| exposure | 0.2624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
