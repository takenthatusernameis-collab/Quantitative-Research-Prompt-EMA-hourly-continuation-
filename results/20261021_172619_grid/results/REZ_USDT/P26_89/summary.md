# EMA Hourly Continuation — REZ/USDT P26_89

**Symbol:** REZ/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.9115 |
| net_win_rate | 0.5246 |
| gross_profit_factor | 1.0993 |
| gross_win_rate | 0.5246 |
| sharpe_ratio | -0.6597 |
| sortino_ratio | -0.2115 |
| max_drawdown | 0.4084 |
| cagr | -0.0975 |
| net_avg_win | 90.2374 |
| net_avg_loss | -109.2388 |
| avg_hold_time_bars | 14.1291 |
| exposure | 0.3181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
