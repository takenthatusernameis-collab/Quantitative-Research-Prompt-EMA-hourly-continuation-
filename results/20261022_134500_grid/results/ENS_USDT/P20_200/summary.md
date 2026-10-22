# EMA Hourly Continuation — ENS/USDT P20_200

**Symbol:** ENS/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.5634 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8330 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -3.0084 |
| sortino_ratio | -0.7683 |
| max_drawdown | 0.6493 |
| cagr | -0.3155 |
| net_avg_win | 51.4503 |
| net_avg_loss | -76.8500 |
| avg_hold_time_bars | 44.8843 |
| exposure | 0.6875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
