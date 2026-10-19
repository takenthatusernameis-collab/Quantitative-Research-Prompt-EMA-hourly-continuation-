# EMA Hourly Continuation — DASH/USDT P20_144

**Symbol:** DASH/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.5420 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8958 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -3.8909 |
| sortino_ratio | -1.2555 |
| max_drawdown | 0.7837 |
| cagr | -0.4445 |
| net_avg_win | 38.3596 |
| net_avg_loss | -59.9449 |
| avg_hold_time_bars | 22.8805 |
| exposure | 0.5398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
