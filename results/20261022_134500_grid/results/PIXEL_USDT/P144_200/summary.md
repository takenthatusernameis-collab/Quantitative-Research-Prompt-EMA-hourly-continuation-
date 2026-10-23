# EMA Hourly Continuation — PIXEL/USDT P144_200

**Symbol:** PIXEL/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.5490 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.9037 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -3.6765 |
| sortino_ratio | -0.9734 |
| max_drawdown | 0.6975 |
| cagr | -0.3750 |
| net_avg_win | 52.1832 |
| net_avg_loss | -79.3750 |
| avg_hold_time_bars | 5.3652 |
| exposure | 0.0864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
