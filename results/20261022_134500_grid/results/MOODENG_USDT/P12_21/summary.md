# EMA Hourly Continuation — MOODENG/USDT P12_21

**Symbol:** MOODENG/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1213 |
| net_profit_factor | 0.5177 |
| net_win_rate | 0.4138 |
| gross_profit_factor | 0.8567 |
| gross_win_rate | 0.4386 |
| sharpe_ratio | -11.4767 |
| sortino_ratio | -6.2147 |
| max_drawdown | 0.9987 |
| cagr | -0.9570 |
| net_avg_win | 21.3488 |
| net_avg_loss | -29.1166 |
| avg_hold_time_bars | 2.5392 |
| exposure | 0.1704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
