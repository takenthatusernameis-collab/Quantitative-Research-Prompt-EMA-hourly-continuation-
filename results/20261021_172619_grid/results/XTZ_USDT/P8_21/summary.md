# EMA Hourly Continuation — XTZ/USDT P8_21

**Symbol:** XTZ/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.6132 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9363 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -3.5463 |
| sortino_ratio | -1.2973 |
| max_drawdown | 0.7748 |
| cagr | -0.4457 |
| net_avg_win | 38.3935 |
| net_avg_loss | -61.0849 |
| avg_hold_time_bars | 5.6486 |
| exposure | 0.1659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
