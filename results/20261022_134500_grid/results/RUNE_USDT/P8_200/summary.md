# EMA Hourly Continuation — RUNE/USDT P8_200

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.6311 |
| net_win_rate | 0.4696 |
| gross_profit_factor | 0.9202 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -2.6562 |
| sortino_ratio | -0.6862 |
| max_drawdown | 0.5881 |
| cagr | -0.2860 |
| net_avg_win | 60.2924 |
| net_avg_loss | -84.5683 |
| avg_hold_time_bars | 51.1768 |
| exposure | 0.8025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
