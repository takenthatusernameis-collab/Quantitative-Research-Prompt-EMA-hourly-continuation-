# EMA Hourly Continuation — ALGO/USDT P34_55

**Symbol:** ALGO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 842 |
| net_profit_factor | 0.4538 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 1.0023 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -6.4844 |
| sortino_ratio | -2.6790 |
| max_drawdown | 0.9638 |
| cagr | -0.7248 |
| net_avg_win | 19.6631 |
| net_avg_loss | -40.3476 |
| avg_hold_time_bars | 2.8860 |
| exposure | 0.1105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
