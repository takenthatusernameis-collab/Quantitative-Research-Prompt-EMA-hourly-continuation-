# EMA Hourly Continuation — JTO/USDT P34_55

**Symbol:** JTO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6718 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.8883 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -2.5147 |
| sortino_ratio | -0.6966 |
| max_drawdown | 0.5743 |
| cagr | -0.2734 |
| net_avg_win | 64.1574 |
| net_avg_loss | -83.6225 |
| avg_hold_time_bars | 6.2918 |
| exposure | 0.1078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
