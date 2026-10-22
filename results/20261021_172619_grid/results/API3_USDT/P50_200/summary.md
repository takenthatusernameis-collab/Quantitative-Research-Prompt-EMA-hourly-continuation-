# EMA Hourly Continuation — API3/USDT P50_200

**Symbol:** API3/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.8337 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0149 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -1.0084 |
| sortino_ratio | -0.2524 |
| max_drawdown | 0.3367 |
| cagr | -0.1111 |
| net_avg_win | 83.3450 |
| net_avg_loss | -101.2898 |
| avg_hold_time_bars | 29.9281 |
| exposure | 0.4163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
