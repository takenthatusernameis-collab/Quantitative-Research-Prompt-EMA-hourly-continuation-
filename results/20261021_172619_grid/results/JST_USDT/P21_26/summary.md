# EMA Hourly Continuation — JST/USDT P21_26

**Symbol:** JST/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.3290 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.8461 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -4.6921 |
| sortino_ratio | -1.0787 |
| max_drawdown | 0.7311 |
| cagr | -0.4058 |
| net_avg_win | 32.5932 |
| net_avg_loss | -76.7314 |
| avg_hold_time_bars | 5.3532 |
| exposure | 0.0610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
