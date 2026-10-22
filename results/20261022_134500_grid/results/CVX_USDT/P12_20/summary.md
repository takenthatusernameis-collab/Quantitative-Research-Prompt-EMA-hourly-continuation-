# EMA Hourly Continuation — CVX/USDT P12_20

**Symbol:** CVX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1524 |
| net_profit_factor | 0.3270 |
| net_win_rate | 0.4016 |
| gross_profit_factor | 0.7994 |
| gross_win_rate | 0.4291 |
| sharpe_ratio | -13.1288 |
| sortino_ratio | -7.2774 |
| max_drawdown | 0.9999 |
| cagr | -0.9760 |
| net_avg_win | 7.9383 |
| net_avg_loss | -16.2910 |
| avg_hold_time_bars | 2.3852 |
| exposure | 0.1652 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
