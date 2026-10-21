# EMA Hourly Continuation — IOTA/USDT P8_144

**Symbol:** IOTA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.9339 |
| net_win_rate | 0.5309 |
| gross_profit_factor | 1.1219 |
| gross_win_rate | 0.5309 |
| sharpe_ratio | -0.3550 |
| sortino_ratio | -0.1031 |
| max_drawdown | 0.2168 |
| cagr | -0.0519 |
| net_avg_win | 82.3387 |
| net_avg_loss | -99.7627 |
| avg_hold_time_bars | 39.7309 |
| exposure | 0.7314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
