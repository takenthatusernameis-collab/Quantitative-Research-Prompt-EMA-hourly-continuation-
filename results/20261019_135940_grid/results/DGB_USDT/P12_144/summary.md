# EMA Hourly Continuation — DGB/USDT P12_144

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5812 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.8835 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -4.5878 |
| sortino_ratio | -1.6223 |
| max_drawdown | 0.8667 |
| cagr | -0.5430 |
| net_avg_win | 41.7339 |
| net_avg_loss | -58.6765 |
| avg_hold_time_bars | 22.3805 |
| exposure | 0.6470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
