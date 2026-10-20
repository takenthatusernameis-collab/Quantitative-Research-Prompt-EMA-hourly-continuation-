# EMA Hourly Continuation — DBR/USDT P26_200

**Symbol:** DBR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.4839 |
| net_win_rate | 0.4225 |
| gross_profit_factor | 0.7620 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -4.4599 |
| sortino_ratio | -1.2638 |
| max_drawdown | 0.7189 |
| cagr | -0.4616 |
| net_avg_win | 47.9943 |
| net_avg_loss | -72.5544 |
| avg_hold_time_bars | 28.7295 |
| exposure | 0.5375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
