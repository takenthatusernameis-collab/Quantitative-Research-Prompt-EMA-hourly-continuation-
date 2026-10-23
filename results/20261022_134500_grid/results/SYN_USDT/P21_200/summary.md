# EMA Hourly Continuation — SYN/USDT P21_200

**Symbol:** SYN/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.7772 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0230 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -1.4047 |
| sortino_ratio | -0.3834 |
| max_drawdown | 0.4502 |
| cagr | -0.1684 |
| net_avg_win | 68.4107 |
| net_avg_loss | -89.4474 |
| avg_hold_time_bars | 37.3227 |
| exposure | 0.6362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
