# EMA Hourly Continuation — XNO/USDT P34_100

**Symbol:** XNO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6237 |
| net_win_rate | 0.4358 |
| gross_profit_factor | 0.7934 |
| gross_win_rate | 0.4358 |
| sharpe_ratio | -3.3516 |
| sortino_ratio | -1.0101 |
| max_drawdown | 0.6939 |
| cagr | -0.3714 |
| net_avg_win | 57.9036 |
| net_avg_loss | -71.7272 |
| avg_hold_time_bars | 11.2434 |
| exposure | 0.2310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
