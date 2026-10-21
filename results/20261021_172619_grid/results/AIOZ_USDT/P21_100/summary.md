# EMA Hourly Continuation — AIOZ/USDT P21_100

**Symbol:** AIOZ/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.9064 |
| net_win_rate | 0.5238 |
| gross_profit_factor | 1.0883 |
| gross_win_rate | 0.5238 |
| sharpe_ratio | -0.6024 |
| sortino_ratio | -0.1822 |
| max_drawdown | 0.2883 |
| cagr | -0.0850 |
| net_avg_win | 83.8077 |
| net_avg_loss | -101.7139 |
| avg_hold_time_bars | 19.7846 |
| exposure | 0.3966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
