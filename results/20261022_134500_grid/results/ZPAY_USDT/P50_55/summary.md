# EMA Hourly Continuation — ZPAY/USDT P50_55

**Symbol:** ZPAY/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 753 |
| net_profit_factor | 0.1886 |
| net_win_rate | 0.2935 |
| gross_profit_factor | 0.4184 |
| gross_win_rate | 0.3081 |
| sharpe_ratio | -10.8560 |
| sortino_ratio | -4.1973 |
| max_drawdown | 0.9952 |
| cagr | -0.8792 |
| net_avg_win | 10.4635 |
| net_avg_loss | -23.0527 |
| avg_hold_time_bars | 5.7304 |
| exposure | 0.1953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
