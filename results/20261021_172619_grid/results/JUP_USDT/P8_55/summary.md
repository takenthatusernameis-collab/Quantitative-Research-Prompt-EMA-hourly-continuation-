# EMA Hourly Continuation — JUP/USDT P8_55

**Symbol:** JUP/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.8050 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9764 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -2.0146 |
| sortino_ratio | -0.7468 |
| max_drawdown | 0.6118 |
| cagr | -0.2917 |
| net_avg_win | 72.6836 |
| net_avg_loss | -86.1078 |
| avg_hold_time_bars | 14.3902 |
| exposure | 0.4409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
