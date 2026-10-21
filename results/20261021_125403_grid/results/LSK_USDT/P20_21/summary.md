# EMA Hourly Continuation — LSK/USDT P20_21

**Symbol:** LSK/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.5934 |
| net_win_rate | 0.4861 |
| gross_profit_factor | 1.0618 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -3.1273 |
| sortino_ratio | -0.8086 |
| max_drawdown | 0.6355 |
| cagr | -0.3119 |
| net_avg_win | 56.5990 |
| net_avg_loss | -90.2113 |
| avg_hold_time_bars | 5.1610 |
| exposure | 0.0758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
