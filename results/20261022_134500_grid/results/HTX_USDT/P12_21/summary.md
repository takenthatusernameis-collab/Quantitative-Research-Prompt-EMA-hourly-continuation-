# EMA Hourly Continuation — HTX/USDT P12_21

**Symbol:** HTX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1625 |
| net_profit_factor | 0.0790 |
| net_win_rate | 0.2018 |
| gross_profit_factor | 0.3798 |
| gross_win_rate | 0.3114 |
| sharpe_ratio | -24.5977 |
| sortino_ratio | -15.8192 |
| max_drawdown | 1.0000 |
| cagr | -0.9998 |
| net_avg_win | 2.6168 |
| net_avg_loss | -8.3719 |
| avg_hold_time_bars | 2.7452 |
| exposure | 0.2019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
