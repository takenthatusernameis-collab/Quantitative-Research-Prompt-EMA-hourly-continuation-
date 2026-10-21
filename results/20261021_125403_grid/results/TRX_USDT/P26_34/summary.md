# EMA Hourly Continuation — TRX/USDT P26_34

**Symbol:** TRX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 125 |
| net_profit_factor | 0.3272 |
| net_win_rate | 0.4240 |
| gross_profit_factor | 0.9360 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -3.7411 |
| sortino_ratio | -0.6243 |
| max_drawdown | 0.5255 |
| cagr | -0.2523 |
| net_avg_win | 47.5453 |
| net_avg_loss | -106.9710 |
| avg_hold_time_bars | 6.0480 |
| exposure | 0.0344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
