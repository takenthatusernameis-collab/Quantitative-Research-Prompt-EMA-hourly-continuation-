# EMA Hourly Continuation — API3/USDT P34_50

**Symbol:** API3/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 972 |
| net_profit_factor | 0.4590 |
| net_win_rate | 0.4300 |
| gross_profit_factor | 0.9407 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -8.7823 |
| sortino_ratio | -3.9006 |
| max_drawdown | 0.9921 |
| cagr | -0.8536 |
| net_avg_win | 20.1313 |
| net_avg_loss | -33.0951 |
| avg_hold_time_bars | 3.0082 |
| exposure | 0.1329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
