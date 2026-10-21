# EMA Hourly Continuation — REZ/USDT P21_26

**Symbol:** REZ/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.5814 |
| net_win_rate | 0.4337 |
| gross_profit_factor | 0.7867 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -2.8788 |
| sortino_ratio | -0.6506 |
| max_drawdown | 0.5546 |
| cagr | -0.2600 |
| net_avg_win | 67.5652 |
| net_avg_loss | -89.0066 |
| avg_hold_time_bars | 5.8996 |
| exposure | 0.0678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
