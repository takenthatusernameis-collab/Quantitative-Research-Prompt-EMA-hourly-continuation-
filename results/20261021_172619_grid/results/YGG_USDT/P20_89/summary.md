# EMA Hourly Continuation — YGG/USDT P20_89

**Symbol:** YGG/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.8461 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0478 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -1.4172 |
| sortino_ratio | -0.4725 |
| max_drawdown | 0.4929 |
| cagr | -0.1972 |
| net_avg_win | 85.0106 |
| net_avg_loss | -103.1020 |
| avg_hold_time_bars | 14.7901 |
| exposure | 0.3634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
