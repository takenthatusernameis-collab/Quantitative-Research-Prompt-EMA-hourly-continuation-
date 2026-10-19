# EMA Hourly Continuation — AKT/USDT P21_200

**Symbol:** AKT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.7538 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0387 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -1.7742 |
| sortino_ratio | -0.5195 |
| max_drawdown | 0.4846 |
| cagr | -0.2210 |
| net_avg_win | 64.8408 |
| net_avg_loss | -89.2627 |
| avg_hold_time_bars | 29.4954 |
| exposure | 0.5792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
