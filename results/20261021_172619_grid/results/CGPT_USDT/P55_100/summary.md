# EMA Hourly Continuation — CGPT/USDT P55_100

**Symbol:** CGPT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.7403 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9525 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -1.7494 |
| sortino_ratio | -0.4558 |
| max_drawdown | 0.4200 |
| cagr | -0.1893 |
| net_avg_win | 72.0797 |
| net_avg_loss | -92.7872 |
| avg_hold_time_bars | 8.0090 |
| exposure | 0.1209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
