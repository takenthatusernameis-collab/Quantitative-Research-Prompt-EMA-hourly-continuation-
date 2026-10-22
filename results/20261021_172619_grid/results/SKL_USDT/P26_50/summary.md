# EMA Hourly Continuation — SKL/USDT P26_50

**Symbol:** SKL/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.6370 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.8531 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -3.2090 |
| sortino_ratio | -0.9515 |
| max_drawdown | 0.6848 |
| cagr | -0.3542 |
| net_avg_win | 59.6791 |
| net_avg_loss | -77.4769 |
| avg_hold_time_bars | 6.8199 |
| exposure | 0.1342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
