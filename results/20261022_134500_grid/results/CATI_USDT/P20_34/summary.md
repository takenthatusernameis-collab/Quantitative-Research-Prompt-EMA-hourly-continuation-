# EMA Hourly Continuation — CATI/USDT P20_34

**Symbol:** CATI/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1079 |
| net_profit_factor | 0.3797 |
| net_win_rate | 0.3661 |
| gross_profit_factor | 0.6806 |
| gross_win_rate | 0.4032 |
| sharpe_ratio | -12.9596 |
| sortino_ratio | -6.6872 |
| max_drawdown | 0.9992 |
| cagr | -0.9665 |
| net_avg_win | 15.4856 |
| net_avg_loss | -23.5502 |
| avg_hold_time_bars | 2.7183 |
| exposure | 0.1608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
