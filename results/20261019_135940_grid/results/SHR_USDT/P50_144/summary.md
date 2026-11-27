# EMA Hourly Continuation — SHR/USDT P50_144

**Symbol:** SHR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.4316 |
| net_win_rate | 0.3329 |
| gross_profit_factor | 0.5669 |
| gross_win_rate | 0.3343 |
| sharpe_ratio | -7.7014 |
| sortino_ratio | -2.8701 |
| max_drawdown | 0.9691 |
| cagr | -0.7452 |
| net_avg_win | 30.8869 |
| net_avg_loss | -35.7096 |
| avg_hold_time_bars | 8.0769 |
| exposure | 0.2613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
