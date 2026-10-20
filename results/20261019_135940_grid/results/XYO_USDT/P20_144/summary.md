# EMA Hourly Continuation — XYO/USDT P20_144

**Symbol:** XYO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.4601 |
| net_win_rate | 0.4046 |
| gross_profit_factor | 0.7590 |
| gross_win_rate | 0.4127 |
| sharpe_ratio | -6.5597 |
| sortino_ratio | -2.2692 |
| max_drawdown | 0.9446 |
| cagr | -0.6769 |
| net_avg_win | 32.3810 |
| net_avg_loss | -47.8137 |
| avg_hold_time_bars | 19.1729 |
| exposure | 0.5318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
