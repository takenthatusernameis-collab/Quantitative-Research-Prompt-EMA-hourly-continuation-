# EMA Hourly Continuation — BIGTIME/USDT P20_21

**Symbol:** BIGTIME/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.5396 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8128 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -2.9250 |
| sortino_ratio | -0.6262 |
| max_drawdown | 0.5210 |
| cagr | -0.2507 |
| net_avg_win | 60.6221 |
| net_avg_loss | -89.8723 |
| avg_hold_time_bars | 5.2178 |
| exposure | 0.0531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
