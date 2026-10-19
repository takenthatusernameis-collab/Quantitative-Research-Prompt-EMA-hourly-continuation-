# EMA Hourly Continuation — ETHFI/USDT P144_200

**Symbol:** ETHFI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.5346 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.8605 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -4.1217 |
| sortino_ratio | -1.2296 |
| max_drawdown | 0.7745 |
| cagr | -0.4460 |
| net_avg_win | 43.7405 |
| net_avg_loss | -68.0730 |
| avg_hold_time_bars | 4.4541 |
| exposure | 0.0905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
