# EMA Hourly Continuation — LSK/USDT P8_100

**Symbol:** LSK/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.6702 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.9629 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -3.4269 |
| sortino_ratio | -1.1696 |
| max_drawdown | 0.7760 |
| cagr | -0.4304 |
| net_avg_win | 55.5206 |
| net_avg_loss | -73.7829 |
| avg_hold_time_bars | 24.7245 |
| exposure | 0.6608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
