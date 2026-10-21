# EMA Hourly Continuation — CRO/USDT P12_144

**Symbol:** CRO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7949 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0338 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -1.3383 |
| sortino_ratio | -0.3760 |
| max_drawdown | 0.3755 |
| cagr | -0.1594 |
| net_avg_win | 69.8833 |
| net_avg_loss | -92.1460 |
| avg_hold_time_bars | 37.2585 |
| exposure | 0.6486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
