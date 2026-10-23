# EMA Hourly Continuation — CELO/USDT P20_55

**Symbol:** CELO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 893 |
| net_profit_factor | 0.4948 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8259 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -6.2287 |
| sortino_ratio | -2.6197 |
| max_drawdown | 0.9590 |
| cagr | -0.7148 |
| net_avg_win | 23.2796 |
| net_avg_loss | -38.6931 |
| avg_hold_time_bars | 6.5454 |
| exposure | 0.2645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
