# EMA Hourly Continuation — CKB/USDT P12_89

**Symbol:** CKB/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.8119 |
| net_win_rate | 0.5009 |
| gross_profit_factor | 1.0044 |
| gross_win_rate | 0.5009 |
| sharpe_ratio | -1.5563 |
| sortino_ratio | -0.5115 |
| max_drawdown | 0.4566 |
| cagr | -0.2113 |
| net_avg_win | 73.4094 |
| net_avg_loss | -90.7658 |
| avg_hold_time_bars | 22.4516 |
| exposure | 0.5378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
