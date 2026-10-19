# EMA Hourly Continuation — XTZ/USDT P100_144

**Symbol:** XTZ/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.4867 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 1.0638 |
| gross_win_rate | 0.5210 |
| sharpe_ratio | -4.6782 |
| sortino_ratio | -1.4910 |
| max_drawdown | 0.8352 |
| cagr | -0.5102 |
| net_avg_win | 32.6525 |
| net_avg_loss | -63.1758 |
| avg_hold_time_bars | 4.3507 |
| exposure | 0.0987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
