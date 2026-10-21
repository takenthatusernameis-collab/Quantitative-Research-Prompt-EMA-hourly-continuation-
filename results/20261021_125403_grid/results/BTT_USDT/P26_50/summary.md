# EMA Hourly Continuation — BTT/USDT P26_50

**Symbol:** BTT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.4477 |
| net_win_rate | 0.4101 |
| gross_profit_factor | 0.7826 |
| gross_win_rate | 0.4101 |
| sharpe_ratio | -5.7718 |
| sortino_ratio | -1.6301 |
| max_drawdown | 0.8563 |
| cagr | -0.5360 |
| net_avg_win | 44.7022 |
| net_avg_loss | -69.3962 |
| avg_hold_time_bars | 8.1376 |
| exposure | 0.1398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
