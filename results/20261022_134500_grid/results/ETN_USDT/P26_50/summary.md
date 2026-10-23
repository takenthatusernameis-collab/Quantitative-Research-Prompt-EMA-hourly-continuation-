# EMA Hourly Continuation — ETN/USDT P26_50

**Symbol:** ETN/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 873 |
| net_profit_factor | 0.2530 |
| net_win_rate | 0.3310 |
| gross_profit_factor | 0.4324 |
| gross_win_rate | 0.3471 |
| sharpe_ratio | -12.6082 |
| sortino_ratio | -5.7817 |
| max_drawdown | 0.9981 |
| cagr | -0.9492 |
| net_avg_win | 11.6997 |
| net_avg_loss | -22.8803 |
| avg_hold_time_bars | 4.0997 |
| exposure | 0.1944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
