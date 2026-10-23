# EMA Hourly Continuation — VELO/USDT P55_200

**Symbol:** VELO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7795 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0126 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -1.4870 |
| sortino_ratio | -0.4437 |
| max_drawdown | 0.4702 |
| cagr | -0.1865 |
| net_avg_win | 64.6985 |
| net_avg_loss | -85.7155 |
| avg_hold_time_bars | 17.5103 |
| exposure | 0.3462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
