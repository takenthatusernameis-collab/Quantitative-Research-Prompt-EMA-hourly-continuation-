# EMA Hourly Continuation — ONDO/USDT P50_55

**Symbol:** ONDO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 83 |
| net_profit_factor | 0.6490 |
| net_win_rate | 0.4578 |
| gross_profit_factor | 0.8487 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -1.2500 |
| sortino_ratio | -0.1621 |
| max_drawdown | 0.2201 |
| cagr | -0.0719 |
| net_avg_win | 83.1548 |
| net_avg_loss | -108.2010 |
| avg_hold_time_bars | 8.4578 |
| exposure | 0.0319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
