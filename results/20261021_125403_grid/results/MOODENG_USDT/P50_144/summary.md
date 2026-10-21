# EMA Hourly Continuation — MOODENG/USDT P50_144

**Symbol:** MOODENG/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.8182 |
| net_win_rate | 0.4910 |
| gross_profit_factor | 0.9677 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -1.1862 |
| sortino_ratio | -0.3123 |
| max_drawdown | 0.2931 |
| cagr | -0.1354 |
| net_avg_win | 85.1416 |
| net_avg_loss | -100.3994 |
| avg_hold_time_bars | 18.7384 |
| exposure | 0.2893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
