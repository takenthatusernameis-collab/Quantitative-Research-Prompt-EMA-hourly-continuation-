# EMA Hourly Continuation — SYN/USDT P34_144

**Symbol:** SYN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.7932 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.1047 |
| gross_win_rate | 0.5193 |
| sharpe_ratio | -1.6715 |
| sortino_ratio | -0.5119 |
| max_drawdown | 0.5120 |
| cagr | -0.2166 |
| net_avg_win | 72.9568 |
| net_avg_loss | -98.5136 |
| avg_hold_time_bars | 21.4721 |
| exposure | 0.4548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
