# EMA Hourly Continuation — API3/USDT P50_200

**Symbol:** API3/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7437 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 0.9999 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -1.9168 |
| sortino_ratio | -0.5265 |
| max_drawdown | 0.5114 |
| cagr | -0.2195 |
| net_avg_win | 72.2793 |
| net_avg_loss | -95.1445 |
| avg_hold_time_bars | 24.7926 |
| exposure | 0.4237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
