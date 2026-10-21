# EMA Hourly Continuation — ATOM/USDT P89_100

**Symbol:** ATOM/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 77 |
| net_profit_factor | 0.8165 |
| net_win_rate | 0.5584 |
| gross_profit_factor | 1.2428 |
| gross_win_rate | 0.5584 |
| sharpe_ratio | -0.4908 |
| sortino_ratio | -0.0627 |
| max_drawdown | 0.1420 |
| cagr | -0.0283 |
| net_avg_win | 72.0853 |
| net_avg_loss | -111.6564 |
| avg_hold_time_bars | 3.7662 |
| exposure | 0.0132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
