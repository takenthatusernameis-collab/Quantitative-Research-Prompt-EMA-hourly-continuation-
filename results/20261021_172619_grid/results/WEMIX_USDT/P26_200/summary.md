# EMA Hourly Continuation — WEMIX/USDT P26_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.4743 |
| net_win_rate | 0.3666 |
| gross_profit_factor | 0.5843 |
| gross_win_rate | 0.3666 |
| sharpe_ratio | -4.3776 |
| sortino_ratio | -1.1346 |
| max_drawdown | 0.7354 |
| cagr | -0.4100 |
| net_avg_win | 52.9806 |
| net_avg_loss | -64.6491 |
| avg_hold_time_bars | 38.1525 |
| exposure | 0.5914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
