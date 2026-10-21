# EMA Hourly Continuation — DBR/USDT P26_50

**Symbol:** DBR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.5718 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.8869 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -3.5373 |
| sortino_ratio | -0.9840 |
| max_drawdown | 0.6156 |
| cagr | -0.3638 |
| net_avg_win | 57.3113 |
| net_avg_loss | -85.4708 |
| avg_hold_time_bars | 9.7517 |
| exposure | 0.1675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
