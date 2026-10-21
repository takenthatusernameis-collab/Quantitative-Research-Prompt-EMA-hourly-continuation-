# EMA Hourly Continuation — BTC/USDT P50_89

**Symbol:** BTC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.5178 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9936 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -3.3101 |
| sortino_ratio | -0.8179 |
| max_drawdown | 0.6579 |
| cagr | -0.3116 |
| net_avg_win | 42.9178 |
| net_avg_loss | -81.3929 |
| avg_hold_time_bars | 8.7734 |
| exposure | 0.1162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
