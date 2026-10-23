# EMA Hourly Continuation — EWT/USDT P50_89

**Symbol:** EWT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.4235 |
| net_win_rate | 0.4058 |
| gross_profit_factor | 0.7508 |
| gross_win_rate | 0.4156 |
| sharpe_ratio | -7.0161 |
| sortino_ratio | -2.4563 |
| max_drawdown | 0.9559 |
| cagr | -0.7072 |
| net_avg_win | 28.0382 |
| net_avg_loss | -45.2247 |
| avg_hold_time_bars | 4.9383 |
| exposure | 0.1383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
