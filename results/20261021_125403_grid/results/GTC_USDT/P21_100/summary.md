# EMA Hourly Continuation — GTC/USDT P21_100

**Symbol:** GTC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.7155 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.8974 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -2.3430 |
| sortino_ratio | -0.7553 |
| max_drawdown | 0.6050 |
| cagr | -0.2938 |
| net_avg_win | 60.0430 |
| net_avg_loss | -76.1200 |
| avg_hold_time_bars | 16.2846 |
| exposure | 0.3797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
