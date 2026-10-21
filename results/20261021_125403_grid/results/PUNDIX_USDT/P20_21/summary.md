# EMA Hourly Continuation — PUNDIX/USDT P20_21

**Symbol:** PUNDIX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.4545 |
| net_win_rate | 0.4371 |
| gross_profit_factor | 0.7581 |
| gross_win_rate | 0.4371 |
| sharpe_ratio | -4.1291 |
| sortino_ratio | -1.0326 |
| max_drawdown | 0.7100 |
| cagr | -0.3811 |
| net_avg_win | 44.2076 |
| net_avg_loss | -75.5217 |
| avg_hold_time_bars | 5.5066 |
| exposure | 0.0756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
