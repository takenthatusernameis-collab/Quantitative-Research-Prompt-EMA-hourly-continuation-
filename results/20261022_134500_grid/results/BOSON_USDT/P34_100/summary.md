# EMA Hourly Continuation — BOSON/USDT P34_100

**Symbol:** BOSON/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.6202 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.8765 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -4.0646 |
| sortino_ratio | -1.4507 |
| max_drawdown | 0.8217 |
| cagr | -0.4967 |
| net_avg_win | 46.1095 |
| net_avg_loss | -61.2891 |
| avg_hold_time_bars | 9.7966 |
| exposure | 0.2868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
