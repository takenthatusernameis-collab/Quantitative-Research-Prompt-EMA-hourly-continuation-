# EMA Hourly Continuation — PYTH/USDT P89_144

**Symbol:** PYTH/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.8381 |
| net_win_rate | 0.5217 |
| gross_profit_factor | 1.0711 |
| gross_win_rate | 0.5217 |
| sharpe_ratio | -0.8011 |
| sortino_ratio | -0.1837 |
| max_drawdown | 0.2696 |
| cagr | -0.0821 |
| net_avg_win | 75.8903 |
| net_avg_loss | -98.7855 |
| avg_hold_time_bars | 7.3755 |
| exposure | 0.0848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
