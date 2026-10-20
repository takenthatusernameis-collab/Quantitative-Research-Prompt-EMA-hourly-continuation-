# EMA Hourly Continuation — NOT/USDT P34_50

**Symbol:** NOT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 944 |
| net_profit_factor | 0.4355 |
| net_win_rate | 0.4174 |
| gross_profit_factor | 0.8122 |
| gross_win_rate | 0.4333 |
| sharpe_ratio | -9.4407 |
| sortino_ratio | -4.1835 |
| max_drawdown | 0.9949 |
| cagr | -0.8801 |
| net_avg_win | 19.4697 |
| net_avg_loss | -32.0243 |
| avg_hold_time_bars | 2.5117 |
| exposure | 0.1114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
