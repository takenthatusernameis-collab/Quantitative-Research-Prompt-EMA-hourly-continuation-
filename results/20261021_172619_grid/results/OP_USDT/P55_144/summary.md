# EMA Hourly Continuation — OP/USDT P55_144

**Symbol:** OP/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7358 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9178 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -1.8643 |
| sortino_ratio | -0.4863 |
| max_drawdown | 0.4675 |
| cagr | -0.2001 |
| net_avg_win | 75.1869 |
| net_avg_loss | -92.3095 |
| avg_hold_time_bars | 15.6806 |
| exposure | 0.2388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
