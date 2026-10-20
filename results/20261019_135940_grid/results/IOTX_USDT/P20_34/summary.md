# EMA Hourly Continuation — IOTX/USDT P20_34

**Symbol:** IOTX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1136 |
| net_profit_factor | 0.4011 |
| net_win_rate | 0.4243 |
| gross_profit_factor | 0.8736 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -10.6359 |
| sortino_ratio | -5.1292 |
| max_drawdown | 0.9985 |
| cagr | -0.9240 |
| net_avg_win | 13.8755 |
| net_avg_loss | -25.4931 |
| avg_hold_time_bars | 2.7245 |
| exposure | 0.1407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
