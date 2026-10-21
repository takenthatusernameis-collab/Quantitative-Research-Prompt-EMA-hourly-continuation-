# EMA Hourly Continuation — MTL/USDT P8_21

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 811 |
| net_profit_factor | 0.6069 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9637 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -5.2948 |
| sortino_ratio | -2.1594 |
| max_drawdown | 0.9210 |
| cagr | -0.6307 |
| net_avg_win | 36.5725 |
| net_avg_loss | -55.2708 |
| avg_hold_time_bars | 6.5401 |
| exposure | 0.2400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
