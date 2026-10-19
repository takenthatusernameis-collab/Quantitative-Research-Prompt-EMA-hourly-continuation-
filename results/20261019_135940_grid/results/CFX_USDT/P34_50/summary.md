# EMA Hourly Continuation — CFX/USDT P34_50

**Symbol:** CFX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 952 |
| net_profit_factor | 0.3800 |
| net_win_rate | 0.4191 |
| gross_profit_factor | 0.8000 |
| gross_win_rate | 0.4328 |
| sharpe_ratio | -9.9510 |
| sortino_ratio | -4.3578 |
| max_drawdown | 0.9964 |
| cagr | -0.8929 |
| net_avg_win | 15.3043 |
| net_avg_loss | -29.0594 |
| avg_hold_time_bars | 2.7311 |
| exposure | 0.1182 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
