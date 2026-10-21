# EMA Hourly Continuation — SHIB/USDT P20_144

**Symbol:** SHIB/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.9112 |
| net_win_rate | 0.5348 |
| gross_profit_factor | 1.1574 |
| gross_win_rate | 0.5348 |
| sharpe_ratio | -0.5758 |
| sortino_ratio | -0.1609 |
| max_drawdown | 0.3036 |
| cagr | -0.0745 |
| net_avg_win | 90.6492 |
| net_avg_loss | -114.3503 |
| avg_hold_time_bars | 29.1176 |
| exposure | 0.4950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
