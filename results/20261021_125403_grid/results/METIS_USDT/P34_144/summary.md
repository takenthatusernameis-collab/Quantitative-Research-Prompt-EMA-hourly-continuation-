# EMA Hourly Continuation — METIS/USDT P34_144

**Symbol:** METIS/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6564 |
| net_win_rate | 0.4400 |
| gross_profit_factor | 0.8006 |
| gross_win_rate | 0.4400 |
| sharpe_ratio | -2.6889 |
| sortino_ratio | -0.7367 |
| max_drawdown | 0.5740 |
| cagr | -0.2881 |
| net_avg_win | 66.4645 |
| net_avg_loss | -79.5550 |
| avg_hold_time_bars | 23.1227 |
| exposure | 0.3941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
