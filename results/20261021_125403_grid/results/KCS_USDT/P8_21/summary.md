# EMA Hourly Continuation — KCS/USDT P8_21

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.3786 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.7494 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -6.1929 |
| sortino_ratio | -2.0567 |
| max_drawdown | 0.9141 |
| cagr | -0.6189 |
| net_avg_win | 24.0385 |
| net_avg_loss | -49.7162 |
| avg_hold_time_bars | 7.4525 |
| exposure | 0.1782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
