# EMA Hourly Continuation — DEXE/USDT P12_100

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.6871 |
| net_win_rate | 0.5009 |
| gross_profit_factor | 0.9798 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -2.5311 |
| sortino_ratio | -0.8472 |
| max_drawdown | 0.6612 |
| cagr | -0.3359 |
| net_avg_win | 49.4798 |
| net_avg_loss | -72.2668 |
| avg_hold_time_bars | 25.3339 |
| exposure | 0.6552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
