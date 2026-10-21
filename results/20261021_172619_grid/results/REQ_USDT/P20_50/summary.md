# EMA Hourly Continuation — REQ/USDT P20_50

**Symbol:** REQ/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.6010 |
| net_win_rate | 0.4601 |
| gross_profit_factor | 0.9371 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -4.7835 |
| sortino_ratio | -1.6632 |
| max_drawdown | 0.8571 |
| cagr | -0.5375 |
| net_avg_win | 47.5592 |
| net_avg_loss | -67.4416 |
| avg_hold_time_bars | 8.2394 |
| exposure | 0.2206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
