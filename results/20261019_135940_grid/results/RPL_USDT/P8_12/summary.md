# EMA Hourly Continuation — RPL/USDT P8_12

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1558 |
| net_profit_factor | 0.2852 |
| net_win_rate | 0.4172 |
| gross_profit_factor | 0.9049 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -12.7553 |
| sortino_ratio | -7.1613 |
| max_drawdown | 0.9999 |
| cagr | -0.9738 |
| net_avg_win | 6.1390 |
| net_avg_loss | -15.4067 |
| avg_hold_time_bars | 2.6624 |
| exposure | 0.1877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
