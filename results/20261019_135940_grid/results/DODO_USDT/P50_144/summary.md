# EMA Hourly Continuation — DODO/USDT P50_144

**Symbol:** DODO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 562 |
| net_profit_factor | 0.5276 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.8162 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -4.5531 |
| sortino_ratio | -1.5123 |
| max_drawdown | 0.8427 |
| cagr | -0.5142 |
| net_avg_win | 37.4525 |
| net_avg_loss | -56.8757 |
| avg_hold_time_bars | 10.8096 |
| exposure | 0.2749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
