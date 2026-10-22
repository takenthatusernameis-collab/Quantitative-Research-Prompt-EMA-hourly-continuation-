# EMA Hourly Continuation — ALGO/USDT P21_34

**Symbol:** ALGO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1112 |
| net_profit_factor | 0.3155 |
| net_win_rate | 0.4308 |
| gross_profit_factor | 0.7835 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -10.3746 |
| sortino_ratio | -4.9184 |
| max_drawdown | 0.9982 |
| cagr | -0.9190 |
| net_avg_win | 9.6045 |
| net_avg_loss | -23.0370 |
| avg_hold_time_bars | 2.3498 |
| exposure | 0.1188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
