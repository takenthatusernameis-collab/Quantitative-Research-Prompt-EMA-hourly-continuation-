# EMA Hourly Continuation — INJ/USDT P26_50

**Symbol:** INJ/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.9341 |
| net_win_rate | 0.5492 |
| gross_profit_factor | 1.2118 |
| gross_win_rate | 0.5492 |
| sharpe_ratio | -0.3877 |
| sortino_ratio | -0.1077 |
| max_drawdown | 0.2850 |
| cagr | -0.0527 |
| net_avg_win | 89.5325 |
| net_avg_loss | -116.7662 |
| avg_hold_time_bars | 6.2268 |
| exposure | 0.1036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
