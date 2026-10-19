# EMA Hourly Continuation — KAS/USDT P21_26

**Symbol:** KAS/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1199 |
| net_profit_factor | 0.1527 |
| net_win_rate | 0.3561 |
| gross_profit_factor | 0.5681 |
| gross_win_rate | 0.4220 |
| sharpe_ratio | -14.8387 |
| sortino_ratio | -7.4974 |
| max_drawdown | 1.0000 |
| cagr | -0.9838 |
| net_avg_win | 4.2210 |
| net_avg_loss | -15.2876 |
| avg_hold_time_bars | 1.7648 |
| exposure | 0.0962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
