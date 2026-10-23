# EMA Hourly Continuation — RPL/USDT P34_50

**Symbol:** RPL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 866 |
| net_profit_factor | 0.4716 |
| net_win_rate | 0.4561 |
| gross_profit_factor | 0.9828 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -6.9818 |
| sortino_ratio | -2.9094 |
| max_drawdown | 0.9715 |
| cagr | -0.7545 |
| net_avg_win | 21.9411 |
| net_avg_loss | -39.0179 |
| avg_hold_time_bars | 3.8476 |
| exposure | 0.1508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
