# EMA Hourly Continuation — IMX/USDT P144_200

**Symbol:** IMX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.5702 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9547 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -3.3276 |
| sortino_ratio | -0.9492 |
| max_drawdown | 0.6895 |
| cagr | -0.3620 |
| net_avg_win | 46.1499 |
| net_avg_loss | -75.8715 |
| avg_hold_time_bars | 4.7196 |
| exposure | 0.0861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
