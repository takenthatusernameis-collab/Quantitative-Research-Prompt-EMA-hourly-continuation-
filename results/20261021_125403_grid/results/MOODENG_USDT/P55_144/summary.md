# EMA Hourly Continuation — MOODENG/USDT P55_144

**Symbol:** MOODENG/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.7348 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.8722 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -1.8085 |
| sortino_ratio | -0.4770 |
| max_drawdown | 0.3848 |
| cagr | -0.1976 |
| net_avg_win | 76.6377 |
| net_avg_loss | -91.1719 |
| avg_hold_time_bars | 16.9187 |
| exposure | 0.2649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
