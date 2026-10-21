# EMA Hourly Continuation — BAT/USDT P34_50

**Symbol:** BAT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.5497 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.8767 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -3.3013 |
| sortino_ratio | -0.9176 |
| max_drawdown | 0.6650 |
| cagr | -0.3425 |
| net_avg_win | 44.6457 |
| net_avg_loss | -73.7627 |
| avg_hold_time_bars | 4.5535 |
| exposure | 0.0774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
