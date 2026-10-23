# EMA Hourly Continuation — MOODENG/USDT P55_100

**Symbol:** MOODENG/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.5659 |
| net_win_rate | 0.4544 |
| gross_profit_factor | 0.8252 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -4.5759 |
| sortino_ratio | -1.6513 |
| max_drawdown | 0.8042 |
| cagr | -0.5448 |
| net_avg_win | 42.8978 |
| net_avg_loss | -63.1243 |
| avg_hold_time_bars | 5.4041 |
| exposure | 0.1606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
