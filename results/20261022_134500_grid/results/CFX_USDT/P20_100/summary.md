# EMA Hourly Continuation — CFX/USDT P20_100

**Symbol:** CFX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.6434 |
| net_win_rate | 0.4718 |
| gross_profit_factor | 0.9547 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -3.8570 |
| sortino_ratio | -1.3498 |
| max_drawdown | 0.8189 |
| cagr | -0.4772 |
| net_avg_win | 49.4978 |
| net_avg_loss | -68.7235 |
| avg_hold_time_bars | 15.1014 |
| exposure | 0.4263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
