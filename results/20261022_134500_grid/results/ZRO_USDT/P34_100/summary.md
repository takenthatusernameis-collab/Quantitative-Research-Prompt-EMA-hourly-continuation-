# EMA Hourly Continuation — ZRO/USDT P34_100

**Symbol:** ZRO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.6813 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9641 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -3.3682 |
| sortino_ratio | -1.2578 |
| max_drawdown | 0.7534 |
| cagr | -0.4490 |
| net_avg_win | 51.1355 |
| net_avg_loss | -70.5574 |
| avg_hold_time_bars | 8.3904 |
| exposure | 0.2661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
