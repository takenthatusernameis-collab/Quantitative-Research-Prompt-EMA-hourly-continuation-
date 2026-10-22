# EMA Hourly Continuation — IOTX/USDT P21_144

**Symbol:** IOTX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.7800 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 0.9701 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -1.4728 |
| sortino_ratio | -0.4343 |
| max_drawdown | 0.4179 |
| cagr | -0.1819 |
| net_avg_win | 66.2272 |
| net_avg_loss | -84.5109 |
| avg_hold_time_bars | 24.9812 |
| exposure | 0.4826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
