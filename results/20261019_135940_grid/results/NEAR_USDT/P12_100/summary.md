# EMA Hourly Continuation — NEAR/USDT P12_100

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.6702 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9446 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -3.2505 |
| sortino_ratio | -1.1298 |
| max_drawdown | 0.7509 |
| cagr | -0.4133 |
| net_avg_win | 51.8863 |
| net_avg_loss | -70.5828 |
| avg_hold_time_bars | 21.7145 |
| exposure | 0.5981 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
