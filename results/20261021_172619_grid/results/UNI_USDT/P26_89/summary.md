# EMA Hourly Continuation — UNI/USDT P26_89

**Symbol:** UNI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.6815 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.8581 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -2.3090 |
| sortino_ratio | -0.6809 |
| max_drawdown | 0.5565 |
| cagr | -0.2686 |
| net_avg_win | 57.9254 |
| net_avg_loss | -74.9323 |
| avg_hold_time_bars | 14.7249 |
| exposure | 0.2871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
