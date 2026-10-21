# EMA Hourly Continuation — SUN/USDT P12_20

**Symbol:** SUN/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.3134 |
| net_win_rate | 0.3745 |
| gross_profit_factor | 0.7436 |
| gross_win_rate | 0.4143 |
| sharpe_ratio | -8.5862 |
| sortino_ratio | -2.8254 |
| max_drawdown | 0.9705 |
| cagr | -0.7525 |
| net_avg_win | 23.5652 |
| net_avg_loss | -45.0159 |
| avg_hold_time_bars | 5.8167 |
| exposure | 0.1321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
