# EMA Hourly Continuation — CATI/USDT P8_21

**Symbol:** CATI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.6392 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8460 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -2.9954 |
| sortino_ratio | -0.9306 |
| max_drawdown | 0.6009 |
| cagr | -0.3483 |
| net_avg_win | 57.1211 |
| net_avg_loss | -77.5046 |
| avg_hold_time_bars | 6.8934 |
| exposure | 0.1489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
