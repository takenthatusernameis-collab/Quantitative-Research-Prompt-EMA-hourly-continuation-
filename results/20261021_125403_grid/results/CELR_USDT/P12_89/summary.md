# EMA Hourly Continuation — CELR/USDT P12_89

**Symbol:** CELR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.7115 |
| net_win_rate | 0.4594 |
| gross_profit_factor | 0.8826 |
| gross_win_rate | 0.4594 |
| sharpe_ratio | -2.8309 |
| sortino_ratio | -0.9337 |
| max_drawdown | 0.6856 |
| cagr | -0.3490 |
| net_avg_win | 65.5192 |
| net_avg_loss | -78.2528 |
| avg_hold_time_bars | 21.9760 |
| exposure | 0.5390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
