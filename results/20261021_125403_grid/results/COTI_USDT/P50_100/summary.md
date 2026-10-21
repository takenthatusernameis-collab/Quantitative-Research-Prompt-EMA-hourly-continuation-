# EMA Hourly Continuation — COTI/USDT P50_100

**Symbol:** COTI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.8882 |
| net_win_rate | 0.5382 |
| gross_profit_factor | 1.1439 |
| gross_win_rate | 0.5382 |
| sharpe_ratio | -0.5854 |
| sortino_ratio | -0.1592 |
| max_drawdown | 0.2889 |
| cagr | -0.0735 |
| net_avg_win | 73.0001 |
| net_avg_loss | -95.7999 |
| avg_hold_time_bars | 8.5354 |
| exposure | 0.1370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
