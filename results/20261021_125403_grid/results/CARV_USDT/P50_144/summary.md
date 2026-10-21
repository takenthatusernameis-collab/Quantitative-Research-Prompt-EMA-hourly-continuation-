# EMA Hourly Continuation — CARV/USDT P50_144

**Symbol:** CARV/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.6459 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.8544 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -2.4681 |
| sortino_ratio | -0.6317 |
| max_drawdown | 0.4522 |
| cagr | -0.2503 |
| net_avg_win | 67.2812 |
| net_avg_loss | -88.0239 |
| avg_hold_time_bars | 15.9351 |
| exposure | 0.2349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
