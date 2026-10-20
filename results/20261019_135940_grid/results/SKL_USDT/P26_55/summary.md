# EMA Hourly Continuation — SKL/USDT P26_55

**Symbol:** SKL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 967 |
| net_profit_factor | 0.4941 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.9005 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -7.0619 |
| sortino_ratio | -3.1010 |
| max_drawdown | 0.9779 |
| cagr | -0.7761 |
| net_avg_win | 21.8276 |
| net_avg_loss | -36.4252 |
| avg_hold_time_bars | 4.6184 |
| exposure | 0.2030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
