# EMA Hourly Continuation — MOODENG/USDT P12_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.9765 |
| net_win_rate | 0.5351 |
| gross_profit_factor | 1.1712 |
| gross_win_rate | 0.5439 |
| sharpe_ratio | -0.0818 |
| sortino_ratio | -0.0196 |
| max_drawdown | 0.1717 |
| cagr | -0.0141 |
| net_avg_win | 97.8967 |
| net_avg_loss | -115.3901 |
| avg_hold_time_bars | 62.5088 |
| exposure | 0.7886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
