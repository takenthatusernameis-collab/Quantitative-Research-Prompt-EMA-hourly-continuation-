# EMA Hourly Continuation — CTSI/USDT P12_144

**Symbol:** CTSI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.8320 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 1.0281 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -1.2132 |
| sortino_ratio | -0.3456 |
| max_drawdown | 0.4046 |
| cagr | -0.1486 |
| net_avg_win | 82.7264 |
| net_avg_loss | -100.4389 |
| avg_hold_time_bars | 36.5581 |
| exposure | 0.6580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
