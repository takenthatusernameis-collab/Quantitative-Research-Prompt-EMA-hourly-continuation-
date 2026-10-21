# EMA Hourly Continuation — SSV/USDT P12_21

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6831 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9324 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -2.9078 |
| sortino_ratio | -0.8677 |
| max_drawdown | 0.6459 |
| cagr | -0.3285 |
| net_avg_win | 66.6376 |
| net_avg_loss | -85.8306 |
| avg_hold_time_bars | 4.9018 |
| exposure | 0.0972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
