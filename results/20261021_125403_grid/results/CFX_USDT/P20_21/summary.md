# EMA Hourly Continuation — CFX/USDT P20_21

**Symbol:** CFX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 118 |
| net_profit_factor | 0.7604 |
| net_win_rate | 0.5169 |
| gross_profit_factor | 1.0538 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -0.8918 |
| sortino_ratio | -0.1397 |
| max_drawdown | 0.2356 |
| cagr | -0.0621 |
| net_avg_win | 77.3240 |
| net_avg_loss | -108.8304 |
| avg_hold_time_bars | 5.8814 |
| exposure | 0.0315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
