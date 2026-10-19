# EMA Hourly Continuation — LTC/USDT P20_100

**Symbol:** LTC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.4328 |
| net_win_rate | 0.4256 |
| gross_profit_factor | 0.8398 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -6.6533 |
| sortino_ratio | -2.4324 |
| max_drawdown | 0.9521 |
| cagr | -0.6969 |
| net_avg_win | 25.3481 |
| net_avg_loss | -43.3956 |
| avg_hold_time_bars | 13.3988 |
| exposure | 0.4093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
