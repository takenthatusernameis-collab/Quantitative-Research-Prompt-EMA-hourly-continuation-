# EMA Hourly Continuation — MANTA/USDT P26_50

**Symbol:** MANTA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6853 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.9119 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -2.8798 |
| sortino_ratio | -0.8604 |
| max_drawdown | 0.6637 |
| cagr | -0.3271 |
| net_avg_win | 66.9369 |
| net_avg_loss | -85.5742 |
| avg_hold_time_bars | 6.5011 |
| exposure | 0.1297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
