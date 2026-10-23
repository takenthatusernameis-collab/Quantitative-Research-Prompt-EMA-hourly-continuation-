# EMA Hourly Continuation — SATS/USDT P50_144

**Symbol:** SATS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.5453 |
| net_win_rate | 0.4299 |
| gross_profit_factor | 0.7868 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -3.8818 |
| sortino_ratio | -1.1486 |
| max_drawdown | 0.7483 |
| cagr | -0.4172 |
| net_avg_win | 46.9469 |
| net_avg_loss | -64.9146 |
| avg_hold_time_bars | 13.3597 |
| exposure | 0.2672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
