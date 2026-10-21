# EMA Hourly Continuation — IOTA/USDT P50_144

**Symbol:** IOTA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.7125 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.9035 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -2.0860 |
| sortino_ratio | -0.5656 |
| max_drawdown | 0.5084 |
| cagr | -0.2290 |
| net_avg_win | 69.4973 |
| net_avg_loss | -87.3269 |
| avg_hold_time_bars | 15.7431 |
| exposure | 0.2590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
