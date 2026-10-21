# EMA Hourly Continuation — TWT/USDT P89_144

**Symbol:** TWT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.5024 |
| net_win_rate | 0.4366 |
| gross_profit_factor | 0.7597 |
| gross_win_rate | 0.4366 |
| sharpe_ratio | -3.3511 |
| sortino_ratio | -0.7848 |
| max_drawdown | 0.6018 |
| cagr | -0.3027 |
| net_avg_win | 51.4030 |
| net_avg_loss | -79.2711 |
| avg_hold_time_bars | 9.0336 |
| exposure | 0.1100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
