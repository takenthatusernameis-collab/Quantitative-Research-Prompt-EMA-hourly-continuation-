# EMA Hourly Continuation — TAIKO/USDT P8_50

**Symbol:** TAIKO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.8210 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0559 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -1.7794 |
| sortino_ratio | -0.6846 |
| max_drawdown | 0.6353 |
| cagr | -0.2720 |
| net_avg_win | 69.6183 |
| net_avg_loss | -89.6802 |
| avg_hold_time_bars | 13.4993 |
| exposure | 0.4403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
