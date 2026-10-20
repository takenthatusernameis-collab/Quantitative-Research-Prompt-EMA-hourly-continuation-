# EMA Hourly Continuation — MERL/USDT P20_34

**Symbol:** MERL/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1163 |
| net_profit_factor | 0.4433 |
| net_win_rate | 0.4299 |
| gross_profit_factor | 0.7422 |
| gross_win_rate | 0.4385 |
| sharpe_ratio | -8.6300 |
| sortino_ratio | -4.1291 |
| max_drawdown | 0.9944 |
| cagr | -0.8722 |
| net_avg_win | 15.8360 |
| net_avg_loss | -26.9384 |
| avg_hold_time_bars | 2.9544 |
| exposure | 0.1566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
