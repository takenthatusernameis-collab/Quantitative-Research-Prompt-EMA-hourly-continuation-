# EMA Hourly Continuation — HNT/USDT P50_100

**Symbol:** HNT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.7182 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9069 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -1.8580 |
| sortino_ratio | -0.5052 |
| max_drawdown | 0.4827 |
| cagr | -0.2072 |
| net_avg_win | 64.3624 |
| net_avg_loss | -83.4151 |
| avg_hold_time_bars | 10.5207 |
| exposure | 0.1736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
