# EMA Hourly Continuation — RAY/USDT P50_89

**Symbol:** RAY/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.5122 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.8519 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -5.8534 |
| sortino_ratio | -2.1358 |
| max_drawdown | 0.9291 |
| cagr | -0.6461 |
| net_avg_win | 33.3167 |
| net_avg_loss | -50.7806 |
| avg_hold_time_bars | 4.5225 |
| exposure | 0.1369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
