# EMA Hourly Continuation — ZIL/USDT P12_26

**Symbol:** ZIL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1427 |
| net_profit_factor | 0.3197 |
| net_win_rate | 0.4008 |
| gross_profit_factor | 0.8514 |
| gross_win_rate | 0.4366 |
| sharpe_ratio | -12.6128 |
| sortino_ratio | -6.7848 |
| max_drawdown | 0.9998 |
| cagr | -0.9684 |
| net_avg_win | 8.2127 |
| net_avg_loss | -17.1882 |
| avg_hold_time_bars | 2.9040 |
| exposure | 0.1884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
