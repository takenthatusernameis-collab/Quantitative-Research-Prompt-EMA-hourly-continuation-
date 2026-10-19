# EMA Hourly Continuation — POL/USDT P89_200

**Symbol:** POL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.4565 |
| net_win_rate | 0.4107 |
| gross_profit_factor | 0.7180 |
| gross_win_rate | 0.4209 |
| sharpe_ratio | -4.8899 |
| sortino_ratio | -1.3663 |
| max_drawdown | 0.8163 |
| cagr | -0.4870 |
| net_avg_win | 42.4190 |
| net_avg_loss | -64.7576 |
| avg_hold_time_bars | 12.6913 |
| exposure | 0.2261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
