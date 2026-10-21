# EMA Hourly Continuation — TRB/USDT P8_89

**Symbol:** TRB/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.6811 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8362 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -2.4973 |
| sortino_ratio | -0.7746 |
| max_drawdown | 0.6486 |
| cagr | -0.2995 |
| net_avg_win | 57.0153 |
| net_avg_loss | -72.3071 |
| avg_hold_time_bars | 29.2359 |
| exposure | 0.6337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
