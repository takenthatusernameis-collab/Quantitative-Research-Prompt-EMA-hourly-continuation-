# EMA Hourly Continuation — ARPA/USDT P89_100

**Symbol:** ARPA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 209 |
| net_profit_factor | 0.4493 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.7449 |
| gross_win_rate | 0.4306 |
| sharpe_ratio | -3.4373 |
| sortino_ratio | -0.7122 |
| max_drawdown | 0.5636 |
| cagr | -0.2780 |
| net_avg_win | 50.7934 |
| net_avg_loss | -85.5005 |
| avg_hold_time_bars | 5.3828 |
| exposure | 0.0509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
