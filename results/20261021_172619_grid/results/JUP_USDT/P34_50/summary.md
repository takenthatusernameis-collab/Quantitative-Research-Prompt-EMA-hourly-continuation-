# EMA Hourly Continuation — JUP/USDT P34_50

**Symbol:** JUP/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.8697 |
| net_win_rate | 0.5405 |
| gross_profit_factor | 1.1630 |
| gross_win_rate | 0.5405 |
| sharpe_ratio | -0.6497 |
| sortino_ratio | -0.1514 |
| max_drawdown | 0.2401 |
| cagr | -0.0688 |
| net_avg_win | 78.1170 |
| net_avg_loss | -105.6704 |
| avg_hold_time_bars | 5.0927 |
| exposure | 0.0600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
