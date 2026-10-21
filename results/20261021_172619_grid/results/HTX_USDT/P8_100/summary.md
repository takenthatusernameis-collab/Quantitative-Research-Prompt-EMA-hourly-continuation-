# EMA Hourly Continuation — HTX/USDT P8_100

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.5410 |
| net_win_rate | 0.4235 |
| gross_profit_factor | 0.8427 |
| gross_win_rate | 0.4256 |
| sharpe_ratio | -5.4715 |
| sortino_ratio | -1.7033 |
| max_drawdown | 0.8751 |
| cagr | -0.5579 |
| net_avg_win | 50.9045 |
| net_avg_loss | -69.1152 |
| avg_hold_time_bars | 30.1174 |
| exposure | 0.6501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
