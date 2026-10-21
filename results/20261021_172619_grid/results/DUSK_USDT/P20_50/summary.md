# EMA Hourly Continuation — DUSK/USDT P20_50

**Symbol:** DUSK/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.7049 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.9031 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -3.0529 |
| sortino_ratio | -1.0013 |
| max_drawdown | 0.7422 |
| cagr | -0.3694 |
| net_avg_win | 67.4134 |
| net_avg_loss | -80.4169 |
| avg_hold_time_bars | 6.9323 |
| exposure | 0.1676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
