# EMA Hourly Continuation — MOODENG/USDT P55_89

**Symbol:** MOODENG/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.7253 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9291 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -1.8915 |
| sortino_ratio | -0.4912 |
| max_drawdown | 0.4086 |
| cagr | -0.2023 |
| net_avg_win | 75.1460 |
| net_avg_loss | -96.2525 |
| avg_hold_time_bars | 7.0404 |
| exposure | 0.1060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
