# EMA Hourly Continuation — BTC/USDT P50_89

**Symbol:** BTC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.3001 |
| net_win_rate | 0.4070 |
| gross_profit_factor | 1.0036 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -8.8629 |
| sortino_ratio | -3.0944 |
| max_drawdown | 0.9909 |
| cagr | -0.8068 |
| net_avg_win | 15.7961 |
| net_avg_loss | -36.1160 |
| avg_hold_time_bars | 5.2920 |
| exposure | 0.1399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
