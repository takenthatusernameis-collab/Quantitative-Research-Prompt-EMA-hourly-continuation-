# EMA Hourly Continuation — MOODENG/USDT P26_55

**Symbol:** MOODENG/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 805 |
| net_profit_factor | 0.5800 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.8816 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -6.0271 |
| sortino_ratio | -2.6616 |
| max_drawdown | 0.9312 |
| cagr | -0.7207 |
| net_avg_win | 35.0207 |
| net_avg_loss | -50.3368 |
| avg_hold_time_bars | 4.4286 |
| exposure | 0.1973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
