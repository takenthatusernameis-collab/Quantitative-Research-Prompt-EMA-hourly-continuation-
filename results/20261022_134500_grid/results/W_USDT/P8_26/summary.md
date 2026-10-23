# EMA Hourly Continuation — W/USDT P8_26

**Symbol:** W/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1511 |
| net_profit_factor | 0.5820 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9909 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -7.4804 |
| sortino_ratio | -4.0762 |
| max_drawdown | 0.9938 |
| cagr | -0.8647 |
| net_avg_win | 19.3488 |
| net_avg_loss | -29.8601 |
| avg_hold_time_bars | 3.9861 |
| exposure | 0.2738 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
