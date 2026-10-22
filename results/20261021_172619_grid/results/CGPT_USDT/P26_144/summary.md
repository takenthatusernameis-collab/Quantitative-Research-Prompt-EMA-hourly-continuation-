# EMA Hourly Continuation — CGPT/USDT P26_144

**Symbol:** CGPT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.9272 |
| net_win_rate | 0.5242 |
| gross_profit_factor | 1.1006 |
| gross_win_rate | 0.5242 |
| sharpe_ratio | -0.4327 |
| sortino_ratio | -0.1168 |
| max_drawdown | 0.2472 |
| cagr | -0.0566 |
| net_avg_win | 94.1750 |
| net_avg_loss | -111.9059 |
| avg_hold_time_bars | 28.4217 |
| exposure | 0.4535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
