# EMA Hourly Continuation — APT/USDT P26_50

**Symbol:** APT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1003 |
| net_profit_factor | 0.4411 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8837 |
| gross_win_rate | 0.4546 |
| sharpe_ratio | -8.3343 |
| sortino_ratio | -3.7391 |
| max_drawdown | 0.9914 |
| cagr | -0.8441 |
| net_avg_win | 17.6116 |
| net_avg_loss | -31.7095 |
| avg_hold_time_bars | 3.5364 |
| exposure | 0.1612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
