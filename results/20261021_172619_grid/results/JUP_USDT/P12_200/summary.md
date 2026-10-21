# EMA Hourly Continuation — JUP/USDT P12_200

**Symbol:** JUP/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.7296 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8376 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -1.9506 |
| sortino_ratio | -0.5020 |
| max_drawdown | 0.5189 |
| cagr | -0.2075 |
| net_avg_win | 80.0963 |
| net_avg_loss | -89.3869 |
| avg_hold_time_bars | 45.6747 |
| exposure | 0.6893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
