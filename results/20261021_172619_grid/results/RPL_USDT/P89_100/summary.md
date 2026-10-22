# EMA Hourly Continuation — RPL/USDT P89_100

**Symbol:** RPL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.6294 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9606 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -2.1991 |
| sortino_ratio | -0.4633 |
| max_drawdown | 0.4388 |
| cagr | -0.1901 |
| net_avg_win | 66.7168 |
| net_avg_loss | -99.3703 |
| avg_hold_time_bars | 6.0691 |
| exposure | 0.0596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
