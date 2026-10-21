# EMA Hourly Continuation — TWT/USDT P20_200

**Symbol:** TWT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.8876 |
| net_win_rate | 0.5275 |
| gross_profit_factor | 1.1112 |
| gross_win_rate | 0.5275 |
| sharpe_ratio | -0.5956 |
| sortino_ratio | -0.1509 |
| max_drawdown | 0.2767 |
| cagr | -0.0698 |
| net_avg_win | 80.4738 |
| net_avg_loss | -101.2189 |
| avg_hold_time_bars | 45.6699 |
| exposure | 0.6415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
