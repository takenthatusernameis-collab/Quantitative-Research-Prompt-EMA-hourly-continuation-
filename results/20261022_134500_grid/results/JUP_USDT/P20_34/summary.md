# EMA Hourly Continuation — JUP/USDT P20_34

**Symbol:** JUP/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1142 |
| net_profit_factor | 0.4457 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.9112 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -8.4198 |
| sortino_ratio | -4.0222 |
| max_drawdown | 0.9933 |
| cagr | -0.8630 |
| net_avg_win | 15.2685 |
| net_avg_loss | -28.9459 |
| avg_hold_time_bars | 2.6637 |
| exposure | 0.1383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
