# EMA Hourly Continuation — BNB/USDT P26_55

**Symbol:** BNB/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 936 |
| net_profit_factor | 0.2500 |
| net_win_rate | 0.3846 |
| gross_profit_factor | 0.8296 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -11.9566 |
| sortino_ratio | -5.3012 |
| max_drawdown | 0.9992 |
| cagr | -0.9405 |
| net_avg_win | 9.2532 |
| net_avg_loss | -23.1299 |
| avg_hold_time_bars | 4.1015 |
| exposure | 0.1745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
