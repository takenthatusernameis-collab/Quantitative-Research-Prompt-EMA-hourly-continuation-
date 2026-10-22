# EMA Hourly Continuation — XDC/USDT P20_21

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1240 |
| net_profit_factor | 0.0619 |
| net_win_rate | 0.2169 |
| gross_profit_factor | 0.3859 |
| gross_win_rate | 0.3468 |
| sharpe_ratio | -21.7045 |
| sortino_ratio | -12.7390 |
| max_drawdown | 1.0000 |
| cagr | -0.9993 |
| net_avg_win | 2.4545 |
| net_avg_loss | -10.9786 |
| avg_hold_time_bars | 2.0298 |
| exposure | 0.1144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
