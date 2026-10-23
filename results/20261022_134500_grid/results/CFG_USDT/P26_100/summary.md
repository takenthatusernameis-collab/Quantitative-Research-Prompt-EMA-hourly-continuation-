# EMA Hourly Continuation — CFG/USDT P26_100

**Symbol:** CFG/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.5718 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.8222 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -4.0944 |
| sortino_ratio | -1.3460 |
| max_drawdown | 0.8025 |
| cagr | -0.4687 |
| net_avg_win | 44.6513 |
| net_avg_loss | -61.3322 |
| avg_hold_time_bars | 19.5471 |
| exposure | 0.4807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
