# EMA Hourly Continuation — ONT/USDT P50_89

**Symbol:** ONT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.4616 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.7846 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -5.7932 |
| sortino_ratio | -2.1139 |
| max_drawdown | 0.9239 |
| cagr | -0.6358 |
| net_avg_win | 26.5246 |
| net_avg_loss | -46.4010 |
| avg_hold_time_bars | 5.5262 |
| exposure | 0.1668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
