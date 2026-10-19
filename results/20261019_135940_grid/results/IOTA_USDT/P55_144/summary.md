# EMA Hourly Continuation — IOTA/USDT P55_144

**Symbol:** IOTA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.5405 |
| net_win_rate | 0.4350 |
| gross_profit_factor | 0.8171 |
| gross_win_rate | 0.4414 |
| sharpe_ratio | -4.3374 |
| sortino_ratio | -1.3202 |
| max_drawdown | 0.8075 |
| cagr | -0.4693 |
| net_avg_win | 45.9140 |
| net_avg_loss | -65.3929 |
| avg_hold_time_bars | 11.5117 |
| exposure | 0.2454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
