# EMA Hourly Continuation — W/USDT P89_200

**Symbol:** W/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7204 |
| net_win_rate | 0.5170 |
| gross_profit_factor | 1.0496 |
| gross_win_rate | 0.5170 |
| sharpe_ratio | -1.8052 |
| sortino_ratio | -0.4990 |
| max_drawdown | 0.5009 |
| cagr | -0.2135 |
| net_avg_win | 58.9542 |
| net_avg_loss | -87.5824 |
| avg_hold_time_bars | 11.8616 |
| exposure | 0.2065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
