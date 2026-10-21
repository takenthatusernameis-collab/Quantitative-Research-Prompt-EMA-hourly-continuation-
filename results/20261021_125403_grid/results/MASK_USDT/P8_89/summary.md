# EMA Hourly Continuation — MASK/USDT P8_89

**Symbol:** MASK/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.5413 |
| net_win_rate | 0.4343 |
| gross_profit_factor | 0.7315 |
| gross_win_rate | 0.4378 |
| sharpe_ratio | -4.1753 |
| sortino_ratio | -1.4127 |
| max_drawdown | 0.8157 |
| cagr | -0.4795 |
| net_avg_win | 38.3505 |
| net_avg_loss | -54.3985 |
| avg_hold_time_bars | 24.1103 |
| exposure | 0.6258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
