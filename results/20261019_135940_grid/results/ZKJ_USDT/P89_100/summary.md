# EMA Hourly Continuation — ZKJ/USDT P89_100

**Symbol:** ZKJ/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 777 |
| net_profit_factor | 0.1158 |
| net_win_rate | 0.2716 |
| gross_profit_factor | 0.5340 |
| gross_win_rate | 0.3951 |
| sharpe_ratio | -14.5131 |
| sortino_ratio | -6.2143 |
| max_drawdown | 0.9998 |
| cagr | -0.9669 |
| net_avg_win | 6.2050 |
| net_avg_loss | -19.9776 |
| avg_hold_time_bars | 3.0914 |
| exposure | 0.1092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
