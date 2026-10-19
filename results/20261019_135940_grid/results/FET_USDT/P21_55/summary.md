# EMA Hourly Continuation — FET/USDT P21_55

**Symbol:** FET/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 960 |
| net_profit_factor | 0.5010 |
| net_win_rate | 0.4594 |
| gross_profit_factor | 0.8196 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -6.2690 |
| sortino_ratio | -2.7246 |
| max_drawdown | 0.9648 |
| cagr | -0.7345 |
| net_avg_win | 21.9547 |
| net_avg_loss | -37.2334 |
| avg_hold_time_bars | 5.0927 |
| exposure | 0.2222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
