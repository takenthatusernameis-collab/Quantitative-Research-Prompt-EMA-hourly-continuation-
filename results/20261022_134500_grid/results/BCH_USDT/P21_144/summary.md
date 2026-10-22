# EMA Hourly Continuation — BCH/USDT P21_144

**Symbol:** BCH/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.5395 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.8934 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -4.3840 |
| sortino_ratio | -1.3429 |
| max_drawdown | 0.8192 |
| cagr | -0.4829 |
| net_avg_win | 43.4865 |
| net_avg_loss | -66.5576 |
| avg_hold_time_bars | 24.3237 |
| exposure | 0.5329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
