# EMA Hourly Continuation — FLOW/USDT P55_144

**Symbol:** FLOW/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.6995 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9061 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -2.1817 |
| sortino_ratio | -0.6010 |
| max_drawdown | 0.5097 |
| cagr | -0.2416 |
| net_avg_win | 65.8518 |
| net_avg_loss | -85.0094 |
| avg_hold_time_bars | 15.5871 |
| exposure | 0.2643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
