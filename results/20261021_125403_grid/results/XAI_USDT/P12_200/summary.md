# EMA Hourly Continuation — XAI/USDT P12_200

**Symbol:** XAI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.9855 |
| net_win_rate | 0.5339 |
| gross_profit_factor | 1.1384 |
| gross_win_rate | 0.5339 |
| sharpe_ratio | -0.0264 |
| sortino_ratio | -0.0057 |
| max_drawdown | 0.2239 |
| cagr | -0.0069 |
| net_avg_win | 98.3855 |
| net_avg_loss | -114.3765 |
| avg_hold_time_bars | 80.1674 |
| exposure | 0.8053 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
