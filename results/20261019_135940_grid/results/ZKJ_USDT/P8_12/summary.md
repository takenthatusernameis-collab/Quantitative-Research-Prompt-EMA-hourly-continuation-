# EMA Hourly Continuation — ZKJ/USDT P8_12

**Symbol:** ZKJ/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1950 |
| net_profit_factor | 0.1598 |
| net_win_rate | 0.2354 |
| gross_profit_factor | 0.5191 |
| gross_win_rate | 0.3421 |
| sharpe_ratio | -25.3130 |
| sortino_ratio | -17.1874 |
| max_drawdown | 1.0000 |
| cagr | -0.9999 |
| net_avg_win | 4.1445 |
| net_avg_loss | -7.9828 |
| avg_hold_time_bars | 2.2615 |
| exposure | 0.2005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
