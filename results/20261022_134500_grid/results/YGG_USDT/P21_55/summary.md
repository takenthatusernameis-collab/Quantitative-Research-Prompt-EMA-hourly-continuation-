# EMA Hourly Continuation — YGG/USDT P21_55

**Symbol:** YGG/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.5800 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.9404 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -5.7568 |
| sortino_ratio | -2.4869 |
| max_drawdown | 0.9542 |
| cagr | -0.7001 |
| net_avg_win | 29.4173 |
| net_avg_loss | -44.9805 |
| avg_hold_time_bars | 5.4248 |
| exposure | 0.2334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
