# EMA Hourly Continuation — MANA/USDT P50_100

**Symbol:** MANA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.6544 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.8868 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -2.5894 |
| sortino_ratio | -0.7122 |
| max_drawdown | 0.5604 |
| cagr | -0.2782 |
| net_avg_win | 60.8376 |
| net_avg_loss | -82.1116 |
| avg_hold_time_bars | 8.5337 |
| exposure | 0.1439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
