# EMA Hourly Continuation — STRK/USDT P50_200

**Symbol:** STRK/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.7130 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9966 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.0788 |
| sortino_ratio | -0.5842 |
| max_drawdown | 0.5680 |
| cagr | -0.2439 |
| net_avg_win | 62.9952 |
| net_avg_loss | -88.3471 |
| avg_hold_time_bars | 21.5905 |
| exposure | 0.3906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
