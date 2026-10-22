# EMA Hourly Continuation — IOTA/USDT P34_50

**Symbol:** IOTA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 939 |
| net_profit_factor | 0.3322 |
| net_win_rate | 0.3919 |
| gross_profit_factor | 0.7611 |
| gross_win_rate | 0.4164 |
| sharpe_ratio | -10.6955 |
| sortino_ratio | -4.6917 |
| max_drawdown | 0.9976 |
| cagr | -0.9086 |
| net_avg_win | 13.4863 |
| net_avg_loss | -26.1618 |
| avg_hold_time_bars | 2.6635 |
| exposure | 0.1137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
