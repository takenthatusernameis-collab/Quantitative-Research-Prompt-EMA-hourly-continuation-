# EMA Hourly Continuation — MOODENG/USDT P89_144

**Symbol:** MOODENG/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.7203 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0934 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -2.3324 |
| sortino_ratio | -0.7320 |
| max_drawdown | 0.5172 |
| cagr | -0.2902 |
| net_avg_win | 64.9510 |
| net_avg_loss | -91.5385 |
| avg_hold_time_bars | 5.7870 |
| exposure | 0.1278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
