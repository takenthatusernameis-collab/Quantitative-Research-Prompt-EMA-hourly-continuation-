# EMA Hourly Continuation — JUP/USDT P26_100

**Symbol:** JUP/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.7978 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 0.9639 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.4223 |
| sortino_ratio | -0.4319 |
| max_drawdown | 0.4443 |
| cagr | -0.1816 |
| net_avg_win | 69.6649 |
| net_avg_loss | -85.7864 |
| avg_hold_time_bars | 15.0752 |
| exposure | 0.3097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
