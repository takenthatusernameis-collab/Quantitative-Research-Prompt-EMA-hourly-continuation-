# EMA Hourly Continuation — ONE/USDT P20_100

**Symbol:** ONE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.8558 |
| net_win_rate | 0.5076 |
| gross_profit_factor | 1.0298 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -1.0824 |
| sortino_ratio | -0.3338 |
| max_drawdown | 0.4056 |
| cagr | -0.1448 |
| net_avg_win | 82.0253 |
| net_avg_loss | -98.7903 |
| avg_hold_time_bars | 20.5140 |
| exposure | 0.4317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
