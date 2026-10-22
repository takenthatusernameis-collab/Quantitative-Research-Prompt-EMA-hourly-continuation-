# EMA Hourly Continuation — SAND/USDT P26_89

**Symbol:** SAND/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.5086 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.8354 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -5.5961 |
| sortino_ratio | -2.0541 |
| max_drawdown | 0.9257 |
| cagr | -0.6352 |
| net_avg_win | 31.0386 |
| net_avg_loss | -49.1713 |
| avg_hold_time_bars | 9.7297 |
| exposure | 0.3043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
