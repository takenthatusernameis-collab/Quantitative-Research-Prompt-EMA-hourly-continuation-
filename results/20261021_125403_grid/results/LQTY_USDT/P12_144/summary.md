# EMA Hourly Continuation — LQTY/USDT P12_144

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.8009 |
| net_win_rate | 0.4957 |
| gross_profit_factor | 0.9642 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -1.2239 |
| sortino_ratio | -0.3267 |
| max_drawdown | 0.3467 |
| cagr | -0.1413 |
| net_avg_win | 73.7612 |
| net_avg_loss | -90.5351 |
| avg_hold_time_bars | 43.3789 |
| exposure | 0.6890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
