# EMA Hourly Continuation — KCS/USDT P100_144

**Symbol:** KCS/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 209 |
| net_profit_factor | 0.5120 |
| net_win_rate | 0.5024 |
| gross_profit_factor | 1.0393 |
| gross_win_rate | 0.5167 |
| sharpe_ratio | -2.6659 |
| sortino_ratio | -0.5604 |
| max_drawdown | 0.4939 |
| cagr | -0.2237 |
| net_avg_win | 47.0187 |
| net_avg_loss | -92.7190 |
| avg_hold_time_bars | 9.5120 |
| exposure | 0.0904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
