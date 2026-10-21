# EMA Hourly Continuation — TURBO/USDT P50_144

**Symbol:** TURBO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.9662 |
| net_win_rate | 0.5440 |
| gross_profit_factor | 1.1823 |
| gross_win_rate | 0.5440 |
| sharpe_ratio | -0.1654 |
| sortino_ratio | -0.0459 |
| max_drawdown | 0.2050 |
| cagr | -0.0271 |
| net_avg_win | 95.5655 |
| net_avg_loss | -117.9844 |
| avg_hold_time_bars | 15.7231 |
| exposure | 0.2633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
