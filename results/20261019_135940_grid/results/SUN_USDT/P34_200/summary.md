# EMA Hourly Continuation — SUN/USDT P34_200

**Symbol:** SUN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.4189 |
| net_win_rate | 0.3978 |
| gross_profit_factor | 0.7977 |
| gross_win_rate | 0.4251 |
| sharpe_ratio | -5.5688 |
| sortino_ratio | -1.4907 |
| max_drawdown | 0.8605 |
| cagr | -0.5392 |
| net_avg_win | 42.3748 |
| net_avg_loss | -66.8323 |
| avg_hold_time_bars | 29.9373 |
| exposure | 0.4972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
