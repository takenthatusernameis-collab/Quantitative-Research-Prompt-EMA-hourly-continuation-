# EMA Hourly Continuation — GTC/USDT P20_144

**Symbol:** GTC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.6639 |
| net_win_rate | 0.4601 |
| gross_profit_factor | 0.9200 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -3.2268 |
| sortino_ratio | -1.0460 |
| max_drawdown | 0.7378 |
| cagr | -0.3854 |
| net_avg_win | 57.5756 |
| net_avg_loss | -73.9023 |
| avg_hold_time_bars | 21.9715 |
| exposure | 0.5253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
