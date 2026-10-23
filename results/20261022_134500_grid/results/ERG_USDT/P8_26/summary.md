# EMA Hourly Continuation — ERG/USDT P8_26

**Symbol:** ERG/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1581 |
| net_profit_factor | 0.2675 |
| net_win_rate | 0.3416 |
| gross_profit_factor | 0.5369 |
| gross_win_rate | 0.3612 |
| sharpe_ratio | -15.2706 |
| sortino_ratio | -8.6795 |
| max_drawdown | 1.0000 |
| cagr | -0.9879 |
| net_avg_win | 6.7639 |
| net_avg_loss | -13.1146 |
| avg_hold_time_bars | 3.9222 |
| exposure | 0.2819 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
