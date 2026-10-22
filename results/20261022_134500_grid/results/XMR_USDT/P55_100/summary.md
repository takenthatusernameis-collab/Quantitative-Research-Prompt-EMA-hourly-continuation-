# EMA Hourly Continuation — XMR/USDT P55_100

**Symbol:** XMR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 966 |
| net_profit_factor | 0.2837 |
| net_win_rate | 0.3975 |
| gross_profit_factor | 0.6953 |
| gross_win_rate | 0.4089 |
| sharpe_ratio | -10.5985 |
| sortino_ratio | -4.7117 |
| max_drawdown | 0.9975 |
| cagr | -0.9081 |
| net_avg_win | 10.2904 |
| net_avg_loss | -23.9289 |
| avg_hold_time_bars | 3.3447 |
| exposure | 0.1469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
