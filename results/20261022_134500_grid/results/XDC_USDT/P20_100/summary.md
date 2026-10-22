# EMA Hourly Continuation — XDC/USDT P20_100

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 808 |
| net_profit_factor | 0.3062 |
| net_win_rate | 0.4418 |
| gross_profit_factor | 0.7409 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -7.5642 |
| sortino_ratio | -2.9678 |
| max_drawdown | 0.9814 |
| cagr | -0.7934 |
| net_avg_win | 12.1240 |
| net_avg_loss | -31.3472 |
| avg_hold_time_bars | 9.9752 |
| exposure | 0.3664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
