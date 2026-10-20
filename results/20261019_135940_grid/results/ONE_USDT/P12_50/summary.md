# EMA Hourly Continuation — ONE/USDT P12_50

**Symbol:** ONE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1078 |
| net_profit_factor | 0.5337 |
| net_win_rate | 0.4406 |
| gross_profit_factor | 0.8556 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -7.1588 |
| sortino_ratio | -3.2989 |
| max_drawdown | 0.9832 |
| cagr | -0.7994 |
| net_avg_win | 23.6726 |
| net_avg_loss | -34.9376 |
| avg_hold_time_bars | 7.4583 |
| exposure | 0.3655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
