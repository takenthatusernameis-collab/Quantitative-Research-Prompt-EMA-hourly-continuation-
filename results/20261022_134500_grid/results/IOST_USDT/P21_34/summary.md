# EMA Hourly Continuation — IOST/USDT P21_34

**Symbol:** IOST/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1095 |
| net_profit_factor | 0.2689 |
| net_win_rate | 0.4046 |
| gross_profit_factor | 0.7736 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -11.5047 |
| sortino_ratio | -5.4420 |
| max_drawdown | 0.9992 |
| cagr | -0.9402 |
| net_avg_win | 8.2947 |
| net_avg_loss | -20.9602 |
| avg_hold_time_bars | 3.1142 |
| exposure | 0.1550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
