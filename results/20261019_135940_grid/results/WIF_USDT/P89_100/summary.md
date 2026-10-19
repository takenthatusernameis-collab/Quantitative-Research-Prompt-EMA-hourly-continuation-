# EMA Hourly Continuation — WIF/USDT P89_100

**Symbol:** WIF/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.2722 |
| net_win_rate | 0.3674 |
| gross_profit_factor | 0.5893 |
| gross_win_rate | 0.3937 |
| sharpe_ratio | -9.3811 |
| sortino_ratio | -3.3442 |
| max_drawdown | 0.9869 |
| cagr | -0.8203 |
| net_avg_win | 16.5429 |
| net_avg_loss | -35.2992 |
| avg_hold_time_bars | 2.0659 |
| exposure | 0.0570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
