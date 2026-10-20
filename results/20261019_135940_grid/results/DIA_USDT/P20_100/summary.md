# EMA Hourly Continuation — DIA/USDT P20_100

**Symbol:** DIA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.5991 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8961 |
| gross_win_rate | 0.4633 |
| sharpe_ratio | -4.5851 |
| sortino_ratio | -1.6593 |
| max_drawdown | 0.8752 |
| cagr | -0.5483 |
| net_avg_win | 42.9661 |
| net_avg_loss | -58.9782 |
| avg_hold_time_bars | 14.0465 |
| exposure | 0.4240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
