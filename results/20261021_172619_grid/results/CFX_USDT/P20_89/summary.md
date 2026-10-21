# EMA Hourly Continuation — CFX/USDT P20_89

**Symbol:** CFX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.7895 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 0.9894 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -1.6350 |
| sortino_ratio | -0.4974 |
| max_drawdown | 0.4766 |
| cagr | -0.2051 |
| net_avg_win | 72.9961 |
| net_avg_loss | -91.6493 |
| avg_hold_time_bars | 18.9712 |
| exposure | 0.3898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
