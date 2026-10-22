# EMA Hourly Continuation — NOT/USDT P20_26

**Symbol:** NOT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 134 |
| net_profit_factor | 0.7950 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0524 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -0.8165 |
| sortino_ratio | -0.1383 |
| max_drawdown | 0.1770 |
| cagr | -0.0618 |
| net_avg_win | 80.6676 |
| net_avg_loss | -107.7086 |
| avg_hold_time_bars | 5.9328 |
| exposure | 0.0373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
