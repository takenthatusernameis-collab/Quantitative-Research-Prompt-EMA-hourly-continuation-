# EMA Hourly Continuation — AVAX/USDT P50_89

**Symbol:** AVAX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.7109 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9740 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -1.9966 |
| sortino_ratio | -0.4998 |
| max_drawdown | 0.4593 |
| cagr | -0.2049 |
| net_avg_win | 72.2649 |
| net_avg_loss | -97.0864 |
| avg_hold_time_bars | 7.0328 |
| exposure | 0.0975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
