# EMA Hourly Continuation — DOGE/USDT P20_144

**Symbol:** DOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.5360 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.8369 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -4.5396 |
| sortino_ratio | -1.3186 |
| max_drawdown | 0.8121 |
| cagr | -0.4773 |
| net_avg_win | 49.9293 |
| net_avg_loss | -69.8615 |
| avg_hold_time_bars | 29.7742 |
| exposure | 0.5874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
