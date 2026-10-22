# EMA Hourly Continuation — APE/USDT P21_100

**Symbol:** APE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.6111 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9116 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -3.6872 |
| sortino_ratio | -1.3723 |
| max_drawdown | 0.8192 |
| cagr | -0.4772 |
| net_avg_win | 37.5921 |
| net_avg_loss | -57.5754 |
| avg_hold_time_bars | 12.1281 |
| exposure | 0.3831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
