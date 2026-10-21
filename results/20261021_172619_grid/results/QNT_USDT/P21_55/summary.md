# EMA Hourly Continuation — QNT/USDT P21_55

**Symbol:** QNT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.7111 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0015 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -2.4147 |
| sortino_ratio | -0.8005 |
| max_drawdown | 0.6186 |
| cagr | -0.3061 |
| net_avg_win | 55.1418 |
| net_avg_loss | -78.7237 |
| avg_hold_time_bars | 7.0733 |
| exposure | 0.1710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
