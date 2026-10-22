# EMA Hourly Continuation — EUL/USDT P144_200

**Symbol:** EUL/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.6702 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.8902 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -1.6507 |
| sortino_ratio | -0.3195 |
| max_drawdown | 0.3201 |
| cagr | -0.1362 |
| net_avg_win | 71.8851 |
| net_avg_loss | -96.1976 |
| avg_hold_time_bars | 7.3424 |
| exposure | 0.0614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
