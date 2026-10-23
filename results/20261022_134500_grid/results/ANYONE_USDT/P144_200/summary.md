# EMA Hourly Continuation — ANYONE/USDT P144_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.5323 |
| net_win_rate | 0.4328 |
| gross_profit_factor | 0.7625 |
| gross_win_rate | 0.4418 |
| sharpe_ratio | -3.6019 |
| sortino_ratio | -0.9847 |
| max_drawdown | 0.6604 |
| cagr | -0.3676 |
| net_avg_win | 50.6091 |
| net_avg_loss | -72.5619 |
| avg_hold_time_bars | 5.9254 |
| exposure | 0.1003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
