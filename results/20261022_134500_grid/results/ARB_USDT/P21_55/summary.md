# EMA Hourly Continuation — ARB/USDT P21_55

**Symbol:** ARB/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 904 |
| net_profit_factor | 0.4728 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.8613 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -6.0140 |
| sortino_ratio | -2.5438 |
| max_drawdown | 0.9570 |
| cagr | -0.7119 |
| net_avg_win | 20.2731 |
| net_avg_loss | -37.7054 |
| avg_hold_time_bars | 5.3551 |
| exposure | 0.2200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
