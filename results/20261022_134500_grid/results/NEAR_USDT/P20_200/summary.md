# EMA Hourly Continuation — NEAR/USDT P20_200

**Symbol:** NEAR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.8104 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0489 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -1.3816 |
| sortino_ratio | -0.3744 |
| max_drawdown | 0.4881 |
| cagr | -0.1623 |
| net_avg_win | 83.3865 |
| net_avg_loss | -104.6037 |
| avg_hold_time_bars | 37.9616 |
| exposure | 0.6298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
