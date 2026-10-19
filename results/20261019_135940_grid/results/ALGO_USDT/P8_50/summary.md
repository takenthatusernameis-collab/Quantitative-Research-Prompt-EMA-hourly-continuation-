# EMA Hourly Continuation — ALGO/USDT P8_50

**Symbol:** ALGO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1144 |
| net_profit_factor | 0.5530 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9653 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -5.6972 |
| sortino_ratio | -2.6933 |
| max_drawdown | 0.9653 |
| cagr | -0.7324 |
| net_avg_win | 21.4753 |
| net_avg_loss | -36.5939 |
| avg_hold_time_bars | 8.5087 |
| exposure | 0.4425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
