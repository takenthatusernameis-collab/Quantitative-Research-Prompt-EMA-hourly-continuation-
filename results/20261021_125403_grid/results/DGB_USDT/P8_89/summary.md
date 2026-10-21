# EMA Hourly Continuation — DGB/USDT P8_89

**Symbol:** DGB/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.8513 |
| net_win_rate | 0.5109 |
| gross_profit_factor | 1.0527 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -1.2426 |
| sortino_ratio | -0.4175 |
| max_drawdown | 0.4507 |
| cagr | -0.1770 |
| net_avg_win | 79.0909 |
| net_avg_loss | -97.0707 |
| avg_hold_time_bars | 24.3650 |
| exposure | 0.6069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
