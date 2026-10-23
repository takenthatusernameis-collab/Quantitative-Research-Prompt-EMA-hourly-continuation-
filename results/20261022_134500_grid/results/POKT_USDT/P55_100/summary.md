# EMA Hourly Continuation — POKT/USDT P55_100

**Symbol:** POKT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.4990 |
| net_win_rate | 0.4181 |
| gross_profit_factor | 0.8613 |
| gross_win_rate | 0.4292 |
| sharpe_ratio | -6.7733 |
| sortino_ratio | -2.5572 |
| max_drawdown | 0.9579 |
| cagr | -0.7122 |
| net_avg_win | 31.6646 |
| net_avg_loss | -45.5821 |
| avg_hold_time_bars | 6.0847 |
| exposure | 0.1983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
