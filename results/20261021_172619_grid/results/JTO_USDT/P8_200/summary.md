# EMA Hourly Continuation — JTO/USDT P8_200

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.9301 |
| net_win_rate | 0.5127 |
| gross_profit_factor | 1.0498 |
| gross_win_rate | 0.5127 |
| sharpe_ratio | -0.3706 |
| sortino_ratio | -0.0943 |
| max_drawdown | 0.2818 |
| cagr | -0.0464 |
| net_avg_win | 92.9455 |
| net_avg_loss | -105.1562 |
| avg_hold_time_bars | 54.7325 |
| exposure | 0.7812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
