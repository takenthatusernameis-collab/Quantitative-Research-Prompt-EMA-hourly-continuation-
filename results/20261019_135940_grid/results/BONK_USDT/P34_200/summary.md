# EMA Hourly Continuation — BONK/USDT P34_200

**Symbol:** BONK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.6488 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9048 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -2.5309 |
| sortino_ratio | -0.6834 |
| max_drawdown | 0.6062 |
| cagr | -0.2824 |
| net_avg_win | 59.0165 |
| net_avg_loss | -82.1444 |
| avg_hold_time_bars | 29.3727 |
| exposure | 0.4980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
