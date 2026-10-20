# EMA Hourly Continuation — MOODENG/USDT P26_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.7534 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 1.0193 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -1.6273 |
| sortino_ratio | -0.4008 |
| max_drawdown | 0.3833 |
| cagr | -0.1730 |
| net_avg_win | 80.5634 |
| net_avg_loss | -104.3825 |
| avg_hold_time_bars | 49.5181 |
| exposure | 0.6822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
