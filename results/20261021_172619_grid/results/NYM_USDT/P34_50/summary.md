# EMA Hourly Continuation — NYM/USDT P34_50

**Symbol:** NYM/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.3198 |
| net_win_rate | 0.3927 |
| gross_profit_factor | 0.5891 |
| gross_win_rate | 0.3927 |
| sharpe_ratio | -4.6753 |
| sortino_ratio | -1.0541 |
| max_drawdown | 0.7198 |
| cagr | -0.3940 |
| net_avg_win | 34.6980 |
| net_avg_loss | -70.1550 |
| avg_hold_time_bars | 10.7045 |
| exposure | 0.1202 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
