# EMA Hourly Continuation — SHIB/USDT P55_200

**Symbol:** SHIB/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.5100 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.8365 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -4.2689 |
| sortino_ratio | -1.1393 |
| max_drawdown | 0.7689 |
| cagr | -0.4355 |
| net_avg_win | 49.5818 |
| net_avg_loss | -74.4244 |
| avg_hold_time_bars | 21.9106 |
| exposure | 0.3675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
