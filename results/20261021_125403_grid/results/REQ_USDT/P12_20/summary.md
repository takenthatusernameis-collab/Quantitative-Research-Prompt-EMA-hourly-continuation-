# EMA Hourly Continuation — REQ/USDT P12_20

**Symbol:** REQ/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.4830 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.8644 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -5.5134 |
| sortino_ratio | -1.6791 |
| max_drawdown | 0.8629 |
| cagr | -0.5450 |
| net_avg_win | 41.2756 |
| net_avg_loss | -66.9272 |
| avg_hold_time_bars | 4.8131 |
| exposure | 0.0971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
