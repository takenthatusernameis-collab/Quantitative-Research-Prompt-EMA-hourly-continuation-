# EMA Hourly Continuation — IOTX/USDT P8_100

**Symbol:** IOTX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6285 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9181 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -2.9553 |
| sortino_ratio | -0.8540 |
| max_drawdown | 0.6527 |
| cagr | -0.3354 |
| net_avg_win | 53.4728 |
| net_avg_loss | -78.5027 |
| avg_hold_time_bars | 40.9220 |
| exposure | 0.7868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
