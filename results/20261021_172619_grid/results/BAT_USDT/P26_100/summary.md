# EMA Hourly Continuation — BAT/USDT P26_100

**Symbol:** BAT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.7886 |
| net_win_rate | 0.5107 |
| gross_profit_factor | 1.0468 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -1.6808 |
| sortino_ratio | -0.5468 |
| max_drawdown | 0.5104 |
| cagr | -0.2225 |
| net_avg_win | 66.6952 |
| net_avg_loss | -88.2806 |
| avg_hold_time_bars | 14.5185 |
| exposure | 0.3385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
