# EMA Hourly Continuation — AVAX/USDT P144_200

**Symbol:** AVAX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 178 |
| net_profit_factor | 0.6185 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.8521 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -1.8993 |
| sortino_ratio | -0.3623 |
| max_drawdown | 0.3633 |
| cagr | -0.1526 |
| net_avg_win | 66.4510 |
| net_avg_loss | -93.8698 |
| avg_hold_time_bars | 7.1573 |
| exposure | 0.0579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
