# EMA Hourly Continuation — BLUR/USDT P20_26

**Symbol:** BLUR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.4674 |
| net_win_rate | 0.4070 |
| gross_profit_factor | 0.6666 |
| gross_win_rate | 0.4070 |
| sharpe_ratio | -3.6455 |
| sortino_ratio | -0.8325 |
| max_drawdown | 0.6347 |
| cagr | -0.3190 |
| net_avg_win | 51.8768 |
| net_avg_loss | -76.1617 |
| avg_hold_time_bars | 4.1318 |
| exposure | 0.0482 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
