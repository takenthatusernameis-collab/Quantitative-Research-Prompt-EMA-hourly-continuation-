# EMA Hourly Continuation — DODO/USDT P20_89

**Symbol:** DODO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 770 |
| net_profit_factor | 0.6001 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.9531 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -5.2159 |
| sortino_ratio | -2.0184 |
| max_drawdown | 0.9195 |
| cagr | -0.6243 |
| net_avg_win | 39.4652 |
| net_avg_loss | -54.2360 |
| avg_hold_time_bars | 11.7545 |
| exposure | 0.4096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
