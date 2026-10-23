# EMA Hourly Continuation — AXL/USDT P55_144

**Symbol:** AXL/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.5864 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8307 |
| gross_win_rate | 0.4566 |
| sharpe_ratio | -4.0432 |
| sortino_ratio | -1.3532 |
| max_drawdown | 0.8080 |
| cagr | -0.4711 |
| net_avg_win | 44.4560 |
| net_avg_loss | -62.3574 |
| avg_hold_time_bars | 9.7292 |
| exposure | 0.2487 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
