# EMA Hourly Continuation — VELO/USDT P26_100

**Symbol:** VELO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.9211 |
| net_win_rate | 0.5279 |
| gross_profit_factor | 1.1029 |
| gross_win_rate | 0.5279 |
| sharpe_ratio | -0.4938 |
| sortino_ratio | -0.1536 |
| max_drawdown | 0.3153 |
| cagr | -0.0736 |
| net_avg_win | 82.9225 |
| net_avg_loss | -100.6673 |
| avg_hold_time_bars | 15.0300 |
| exposure | 0.3184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
