# EMA Hourly Continuation — GMX/USDT P21_100

**Symbol:** GMX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.7474 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9609 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -2.3552 |
| sortino_ratio | -0.7720 |
| max_drawdown | 0.6124 |
| cagr | -0.2986 |
| net_avg_win | 68.4078 |
| net_avg_loss | -85.1818 |
| avg_hold_time_bars | 15.7921 |
| exposure | 0.3797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
