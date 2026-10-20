# EMA Hourly Continuation — DEGEN/USDT P8_55

**Symbol:** DEGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 989 |
| net_profit_factor | 0.6911 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.9217 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -4.8243 |
| sortino_ratio | -2.1380 |
| max_drawdown | 0.9215 |
| cagr | -0.6375 |
| net_avg_win | 45.4065 |
| net_avg_loss | -55.7559 |
| avg_hold_time_bars | 10.9757 |
| exposure | 0.4942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
