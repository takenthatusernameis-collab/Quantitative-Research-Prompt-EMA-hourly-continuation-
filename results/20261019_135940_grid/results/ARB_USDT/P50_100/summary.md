# EMA Hourly Continuation — ARB/USDT P50_100

**Symbol:** ARB/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.5562 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9092 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -4.1527 |
| sortino_ratio | -1.4559 |
| max_drawdown | 0.8247 |
| cagr | -0.4986 |
| net_avg_win | 35.0964 |
| net_avg_loss | -58.1555 |
| avg_hold_time_bars | 6.4437 |
| exposure | 0.1795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
