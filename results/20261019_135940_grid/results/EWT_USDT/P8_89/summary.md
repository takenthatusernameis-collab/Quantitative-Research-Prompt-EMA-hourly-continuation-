# EMA Hourly Continuation — EWT/USDT P8_89

**Symbol:** EWT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 825 |
| net_profit_factor | 0.4809 |
| net_win_rate | 0.4230 |
| gross_profit_factor | 0.7355 |
| gross_win_rate | 0.4267 |
| sharpe_ratio | -6.2428 |
| sortino_ratio | -2.5026 |
| max_drawdown | 0.9594 |
| cagr | -0.7059 |
| net_avg_win | 25.3137 |
| net_avg_loss | -38.5964 |
| avg_hold_time_bars | 13.7842 |
| exposure | 0.5169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
