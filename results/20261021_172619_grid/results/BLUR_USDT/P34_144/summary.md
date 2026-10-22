# EMA Hourly Continuation — BLUR/USDT P34_144

**Symbol:** BLUR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.9445 |
| net_win_rate | 0.5398 |
| gross_profit_factor | 1.1756 |
| gross_win_rate | 0.5424 |
| sharpe_ratio | -0.3180 |
| sortino_ratio | -0.0904 |
| max_drawdown | 0.2590 |
| cagr | -0.0463 |
| net_avg_win | 91.3145 |
| net_avg_loss | -113.4231 |
| avg_hold_time_bars | 23.3599 |
| exposure | 0.4112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
