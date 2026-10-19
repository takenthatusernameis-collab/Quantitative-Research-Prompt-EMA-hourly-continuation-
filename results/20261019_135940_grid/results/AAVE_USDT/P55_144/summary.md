# EMA Hourly Continuation — AAVE/USDT P55_144

**Symbol:** AAVE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.5646 |
| net_win_rate | 0.4849 |
| gross_profit_factor | 0.9089 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -3.4709 |
| sortino_ratio | -1.0796 |
| max_drawdown | 0.7620 |
| cagr | -0.4124 |
| net_avg_win | 39.6435 |
| net_avg_loss | -66.1047 |
| avg_hold_time_bars | 11.0946 |
| exposure | 0.2506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
