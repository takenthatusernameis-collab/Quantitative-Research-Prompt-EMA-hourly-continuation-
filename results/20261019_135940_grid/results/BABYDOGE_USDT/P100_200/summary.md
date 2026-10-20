# EMA Hourly Continuation — BABYDOGE/USDT P100_200

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 27 |
| net_profit_factor | 0.8447 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9210 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -0.2633 |
| sortino_ratio | -0.0194 |
| max_drawdown | 0.0564 |
| cagr | -0.0092 |
| net_avg_win | 95.9304 |
| net_avg_loss | -105.4562 |
| avg_hold_time_bars | 24.8889 |
| exposure | 0.0304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
