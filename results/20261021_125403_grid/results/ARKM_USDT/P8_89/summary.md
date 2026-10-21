# EMA Hourly Continuation — ARKM/USDT P8_89

**Symbol:** ARKM/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.8742 |
| net_win_rate | 0.5113 |
| gross_profit_factor | 1.0331 |
| gross_win_rate | 0.5113 |
| sharpe_ratio | -0.8894 |
| sortino_ratio | -0.2809 |
| max_drawdown | 0.3475 |
| cagr | -0.1250 |
| net_avg_win | 79.8025 |
| net_avg_loss | -95.5266 |
| avg_hold_time_bars | 29.2763 |
| exposure | 0.6454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
