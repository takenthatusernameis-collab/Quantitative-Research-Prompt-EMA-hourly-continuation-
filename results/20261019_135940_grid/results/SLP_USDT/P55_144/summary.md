# EMA Hourly Continuation — SLP/USDT P55_144

**Symbol:** SLP/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 572 |
| net_profit_factor | 0.6030 |
| net_win_rate | 0.4633 |
| gross_profit_factor | 0.9437 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -4.2501 |
| sortino_ratio | -1.4323 |
| max_drawdown | 0.8257 |
| cagr | -0.4996 |
| net_avg_win | 47.2407 |
| net_avg_loss | -67.6270 |
| avg_hold_time_bars | 10.5280 |
| exposure | 0.2737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
