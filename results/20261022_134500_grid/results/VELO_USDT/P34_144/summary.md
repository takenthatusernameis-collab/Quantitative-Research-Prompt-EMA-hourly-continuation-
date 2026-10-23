# EMA Hourly Continuation — VELO/USDT P34_144

**Symbol:** VELO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.7378 |
| net_win_rate | 0.4991 |
| gross_profit_factor | 1.0138 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -2.3002 |
| sortino_ratio | -0.7528 |
| max_drawdown | 0.6461 |
| cagr | -0.3034 |
| net_avg_win | 61.9490 |
| net_avg_loss | -83.6564 |
| avg_hold_time_bars | 15.0589 |
| exposure | 0.3717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
