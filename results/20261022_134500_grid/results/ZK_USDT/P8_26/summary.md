# EMA Hourly Continuation — ZK/USDT P8_26

**Symbol:** ZK/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1495 |
| net_profit_factor | 0.5432 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.9186 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -8.7435 |
| sortino_ratio | -4.9337 |
| max_drawdown | 0.9962 |
| cagr | -0.9075 |
| net_avg_win | 17.5016 |
| net_avg_loss | -26.6633 |
| avg_hold_time_bars | 3.6227 |
| exposure | 0.2641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
