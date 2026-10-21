# EMA Hourly Continuation — XEC/USDT P8_89

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.7628 |
| net_win_rate | 0.5009 |
| gross_profit_factor | 0.9930 |
| gross_win_rate | 0.5009 |
| sharpe_ratio | -1.9792 |
| sortino_ratio | -0.6681 |
| max_drawdown | 0.5689 |
| cagr | -0.2650 |
| net_avg_win | 62.0178 |
| net_avg_loss | -81.5946 |
| avg_hold_time_bars | 24.6726 |
| exposure | 0.6241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
