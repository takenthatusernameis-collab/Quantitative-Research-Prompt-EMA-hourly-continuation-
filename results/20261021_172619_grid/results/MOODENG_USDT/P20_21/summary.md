# EMA Hourly Continuation — MOODENG/USDT P20_21

**Symbol:** MOODENG/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 136 |
| net_profit_factor | 0.5382 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.7390 |
| gross_win_rate | 0.4338 |
| sharpe_ratio | -2.3570 |
| sortino_ratio | -0.4314 |
| max_drawdown | 0.3432 |
| cagr | -0.1809 |
| net_avg_win | 66.6487 |
| net_avg_loss | -94.8929 |
| avg_hold_time_bars | 6.6618 |
| exposure | 0.0501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
