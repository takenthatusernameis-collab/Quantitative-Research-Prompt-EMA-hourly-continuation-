# EMA Hourly Continuation — AAVE/USDT P50_144

**Symbol:** AAVE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.9751 |
| net_win_rate | 0.5509 |
| gross_profit_factor | 1.2119 |
| gross_win_rate | 0.5509 |
| sharpe_ratio | -0.0871 |
| sortino_ratio | -0.0231 |
| max_drawdown | 0.1838 |
| cagr | -0.0164 |
| net_avg_win | 86.6105 |
| net_avg_loss | -108.9569 |
| avg_hold_time_bars | 16.8563 |
| exposure | 0.2559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
