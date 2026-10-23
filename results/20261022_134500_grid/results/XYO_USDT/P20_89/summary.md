# EMA Hourly Continuation — XYO/USDT P20_89

**Symbol:** XYO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 823 |
| net_profit_factor | 0.4431 |
| net_win_rate | 0.4131 |
| gross_profit_factor | 0.7759 |
| gross_win_rate | 0.4253 |
| sharpe_ratio | -7.7057 |
| sortino_ratio | -3.0999 |
| max_drawdown | 0.9803 |
| cagr | -0.7859 |
| net_avg_win | 22.9264 |
| net_avg_loss | -36.4185 |
| avg_hold_time_bars | 10.8663 |
| exposure | 0.4047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
