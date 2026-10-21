# EMA Hourly Continuation — SEI/USDT P26_200

**Symbol:** SEI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.9059 |
| net_win_rate | 0.5169 |
| gross_profit_factor | 1.0548 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -0.4653 |
| sortino_ratio | -0.1091 |
| max_drawdown | 0.2130 |
| cagr | -0.0518 |
| net_avg_win | 87.2608 |
| net_avg_loss | -103.0411 |
| avg_hold_time_bars | 49.5094 |
| exposure | 0.6009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
