# EMA Hourly Continuation — TAIKO/USDT P21_144

**Symbol:** TAIKO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6197 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.8888 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -3.0490 |
| sortino_ratio | -0.8926 |
| max_drawdown | 0.6556 |
| cagr | -0.3479 |
| net_avg_win | 53.3088 |
| net_avg_loss | -77.3047 |
| avg_hold_time_bars | 28.3325 |
| exposure | 0.5607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
