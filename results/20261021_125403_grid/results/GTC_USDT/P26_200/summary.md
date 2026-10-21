# EMA Hourly Continuation — GTC/USDT P26_200

**Symbol:** GTC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.7075 |
| net_win_rate | 0.4565 |
| gross_profit_factor | 0.8470 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -2.0118 |
| sortino_ratio | -0.5116 |
| max_drawdown | 0.5048 |
| cagr | -0.2098 |
| net_avg_win | 73.4549 |
| net_avg_loss | -87.2153 |
| avg_hold_time_bars | 36.8571 |
| exposure | 0.5395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
