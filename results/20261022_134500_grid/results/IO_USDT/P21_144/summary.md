# EMA Hourly Continuation — IO/USDT P21_144

**Symbol:** IO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.6204 |
| net_win_rate | 0.4506 |
| gross_profit_factor | 0.8435 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -3.7731 |
| sortino_ratio | -1.2198 |
| max_drawdown | 0.7638 |
| cagr | -0.4491 |
| net_avg_win | 54.0999 |
| net_avg_loss | -71.5201 |
| avg_hold_time_bars | 21.7332 |
| exposure | 0.5324 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
