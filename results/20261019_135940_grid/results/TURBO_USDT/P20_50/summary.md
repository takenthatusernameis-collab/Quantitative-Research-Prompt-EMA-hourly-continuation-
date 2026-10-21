# EMA Hourly Continuation — TURBO/USDT P20_50

**Symbol:** TURBO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 857 |
| net_profit_factor | 0.6304 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.9774 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -6.1472 |
| sortino_ratio | -2.7787 |
| max_drawdown | 0.9427 |
| cagr | -0.7362 |
| net_avg_win | 40.3162 |
| net_avg_loss | -55.1960 |
| avg_hold_time_bars | 4.5228 |
| exposure | 0.2114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
