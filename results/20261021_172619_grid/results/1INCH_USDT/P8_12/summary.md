# EMA Hourly Continuation — 1INCH/USDT P8_12

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.6200 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9875 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -2.6489 |
| sortino_ratio | -0.6539 |
| max_drawdown | 0.5357 |
| cagr | -0.2607 |
| net_avg_win | 59.4061 |
| net_avg_loss | -94.5250 |
| avg_hold_time_bars | 3.9592 |
| exposure | 0.0529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
