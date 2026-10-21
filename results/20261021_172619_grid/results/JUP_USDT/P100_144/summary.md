# EMA Hourly Continuation — JUP/USDT P100_144

**Symbol:** JUP/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 0.7235 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9362 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -1.6081 |
| sortino_ratio | -0.3478 |
| max_drawdown | 0.3782 |
| cagr | -0.1474 |
| net_avg_win | 78.4928 |
| net_avg_loss | -100.2884 |
| avg_hold_time_bars | 6.1572 |
| exposure | 0.0641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
