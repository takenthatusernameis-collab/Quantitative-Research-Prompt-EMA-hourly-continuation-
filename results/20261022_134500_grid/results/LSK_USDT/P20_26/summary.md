# EMA Hourly Continuation — LSK/USDT P20_26

**Symbol:** LSK/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 983 |
| net_profit_factor | 0.3057 |
| net_win_rate | 0.3927 |
| gross_profit_factor | 0.8529 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -10.9783 |
| sortino_ratio | -4.9569 |
| max_drawdown | 0.9982 |
| cagr | -0.9187 |
| net_avg_win | 11.3833 |
| net_avg_loss | -24.0798 |
| avg_hold_time_bars | 3.1892 |
| exposure | 0.1425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
