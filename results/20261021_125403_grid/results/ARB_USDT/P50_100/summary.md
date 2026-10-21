# EMA Hourly Continuation — ARB/USDT P50_100

**Symbol:** ARB/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.7859 |
| net_win_rate | 0.5109 |
| gross_profit_factor | 1.0276 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -1.3306 |
| sortino_ratio | -0.3670 |
| max_drawdown | 0.4401 |
| cagr | -0.1557 |
| net_avg_win | 67.6071 |
| net_avg_loss | -89.8467 |
| avg_hold_time_bars | 9.5951 |
| exposure | 0.1605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
