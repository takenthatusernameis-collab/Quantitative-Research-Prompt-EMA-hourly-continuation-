# EMA Hourly Continuation — CPOOL/USDT P20_55

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 967 |
| net_profit_factor | 0.5545 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8040 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -5.9356 |
| sortino_ratio | -2.5665 |
| max_drawdown | 0.9600 |
| cagr | -0.7199 |
| net_avg_win | 27.1888 |
| net_avg_loss | -40.7704 |
| avg_hold_time_bars | 5.2296 |
| exposure | 0.2299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
