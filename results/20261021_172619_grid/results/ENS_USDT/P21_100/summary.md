# EMA Hourly Continuation — ENS/USDT P21_100

**Symbol:** ENS/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.8375 |
| net_win_rate | 0.5119 |
| gross_profit_factor | 1.0475 |
| gross_win_rate | 0.5119 |
| sharpe_ratio | -1.2159 |
| sortino_ratio | -0.3757 |
| max_drawdown | 0.4280 |
| cagr | -0.1608 |
| net_avg_win | 77.4458 |
| net_avg_loss | -96.9732 |
| avg_hold_time_bars | 20.1296 |
| exposure | 0.4236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
