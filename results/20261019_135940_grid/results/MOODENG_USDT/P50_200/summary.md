# EMA Hourly Continuation — MOODENG/USDT P50_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7674 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9971 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -1.8065 |
| sortino_ratio | -0.4904 |
| max_drawdown | 0.4712 |
| cagr | -0.2084 |
| net_avg_win | 84.0996 |
| net_avg_loss | -106.7505 |
| avg_hold_time_bars | 23.8914 |
| exposure | 0.4019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
