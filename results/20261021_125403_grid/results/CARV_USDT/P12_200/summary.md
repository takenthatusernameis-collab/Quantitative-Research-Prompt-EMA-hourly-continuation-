# EMA Hourly Continuation — CARV/USDT P12_200

**Symbol:** CARV/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.7072 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.8439 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -2.0650 |
| sortino_ratio | -0.5689 |
| max_drawdown | 0.4631 |
| cagr | -0.2309 |
| net_avg_win | 71.2261 |
| net_avg_loss | -85.4571 |
| avg_hold_time_bars | 38.6820 |
| exposure | 0.6639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
