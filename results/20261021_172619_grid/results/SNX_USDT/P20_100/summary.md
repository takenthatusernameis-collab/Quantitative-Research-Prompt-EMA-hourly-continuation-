# EMA Hourly Continuation — SNX/USDT P20_100

**Symbol:** SNX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.9584 |
| net_win_rate | 0.5445 |
| gross_profit_factor | 1.1876 |
| gross_win_rate | 0.5445 |
| sharpe_ratio | -0.2458 |
| sortino_ratio | -0.0781 |
| max_drawdown | 0.2378 |
| cagr | -0.0427 |
| net_avg_win | 91.1951 |
| net_avg_loss | -113.7529 |
| avg_hold_time_bars | 18.0952 |
| exposure | 0.3955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
