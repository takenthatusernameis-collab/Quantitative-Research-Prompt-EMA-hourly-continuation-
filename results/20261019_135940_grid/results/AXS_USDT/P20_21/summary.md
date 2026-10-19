# EMA Hourly Continuation — AXS/USDT P20_21

**Symbol:** AXS/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1159 |
| net_profit_factor | 0.0781 |
| net_win_rate | 0.2899 |
| gross_profit_factor | 0.3953 |
| gross_win_rate | 0.3840 |
| sharpe_ratio | -17.8609 |
| sortino_ratio | -9.3712 |
| max_drawdown | 1.0000 |
| cagr | -0.9950 |
| net_avg_win | 2.5198 |
| net_avg_loss | -13.1794 |
| avg_hold_time_bars | 1.6143 |
| exposure | 0.0847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
