# EMA Hourly Continuation — AVA/USDT P12_50

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.5169 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8703 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -6.8671 |
| sortino_ratio | -3.1436 |
| max_drawdown | 0.9787 |
| cagr | -0.7828 |
| net_avg_win | 21.6272 |
| net_avg_loss | -35.2812 |
| avg_hold_time_bars | 6.4064 |
| exposure | 0.3081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
