# EMA Hourly Continuation — BIGTIME/USDT P50_144

**Symbol:** BIGTIME/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.8770 |
| net_win_rate | 0.5239 |
| gross_profit_factor | 1.1006 |
| gross_win_rate | 0.5239 |
| sharpe_ratio | -0.8094 |
| sortino_ratio | -0.2256 |
| max_drawdown | 0.2942 |
| cagr | -0.1010 |
| net_avg_win | 85.2292 |
| net_avg_loss | -106.9525 |
| avg_hold_time_bars | 16.8963 |
| exposure | 0.2875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
