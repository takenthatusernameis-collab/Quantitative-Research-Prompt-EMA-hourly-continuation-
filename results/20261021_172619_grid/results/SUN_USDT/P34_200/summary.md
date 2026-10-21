# EMA Hourly Continuation — SUN/USDT P34_200

**Symbol:** SUN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.5933 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8726 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -3.1738 |
| sortino_ratio | -0.7758 |
| max_drawdown | 0.6105 |
| cagr | -0.3076 |
| net_avg_win | 65.3098 |
| net_avg_loss | -90.6129 |
| avg_hold_time_bars | 36.3144 |
| exposure | 0.4914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
