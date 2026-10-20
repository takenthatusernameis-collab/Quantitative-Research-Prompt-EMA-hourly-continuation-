# EMA Hourly Continuation — ARKM/USDT P89_144

**Symbol:** ARKM/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.5595 |
| net_win_rate | 0.4584 |
| gross_profit_factor | 0.8626 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -4.3598 |
| sortino_ratio | -1.4329 |
| max_drawdown | 0.8254 |
| cagr | -0.4947 |
| net_avg_win | 41.9941 |
| net_avg_loss | -63.5258 |
| avg_hold_time_bars | 5.0351 |
| exposure | 0.1238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
