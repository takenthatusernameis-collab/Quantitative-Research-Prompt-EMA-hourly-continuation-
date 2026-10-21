# EMA Hourly Continuation — CPOOL/USDT P20_144

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.8559 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9886 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.0176 |
| sortino_ratio | -0.3084 |
| max_drawdown | 0.3856 |
| cagr | -0.1356 |
| net_avg_win | 80.8787 |
| net_avg_loss | -94.4966 |
| avg_hold_time_bars | 21.2489 |
| exposure | 0.4346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
