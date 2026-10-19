# EMA Hourly Continuation — BAT/USDT P26_100

**Symbol:** BAT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.6166 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9920 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -3.6499 |
| sortino_ratio | -1.3283 |
| max_drawdown | 0.7992 |
| cagr | -0.4656 |
| net_avg_win | 40.0952 |
| net_avg_loss | -60.2823 |
| avg_hold_time_bars | 11.6702 |
| exposure | 0.3506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
