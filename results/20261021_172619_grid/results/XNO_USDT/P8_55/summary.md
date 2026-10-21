# EMA Hourly Continuation — XNO/USDT P8_55

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 756 |
| net_profit_factor | 0.6481 |
| net_win_rate | 0.4378 |
| gross_profit_factor | 0.8202 |
| gross_win_rate | 0.4378 |
| sharpe_ratio | -4.2369 |
| sortino_ratio | -1.6510 |
| max_drawdown | 0.8604 |
| cagr | -0.5327 |
| net_avg_win | 47.4064 |
| net_avg_loss | -56.9679 |
| avg_hold_time_bars | 11.2632 |
| exposure | 0.3870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
