# EMA Hourly Continuation — CFG/USDT P8_100

**Symbol:** CFG/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5542 |
| net_win_rate | 0.4434 |
| gross_profit_factor | 0.8025 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -4.1507 |
| sortino_ratio | -1.4684 |
| max_drawdown | 0.8313 |
| cagr | -0.5029 |
| net_avg_win | 36.4639 |
| net_avg_loss | -52.4122 |
| avg_hold_time_bars | 24.1132 |
| exposure | 0.6971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
