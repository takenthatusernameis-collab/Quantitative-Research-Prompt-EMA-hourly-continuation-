# EMA Hourly Continuation — FLR/USDT P8_50

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1304 |
| net_profit_factor | 0.4714 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8831 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -8.9921 |
| sortino_ratio | -4.5173 |
| max_drawdown | 0.9971 |
| cagr | -0.9008 |
| net_avg_win | 15.2248 |
| net_avg_loss | -26.1959 |
| avg_hold_time_bars | 7.5882 |
| exposure | 0.4498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
