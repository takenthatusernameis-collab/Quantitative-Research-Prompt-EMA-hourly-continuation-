# EMA Hourly Continuation — UQC/USDT P21_50

**Symbol:** UQC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.1648 |
| net_win_rate | 0.2871 |
| gross_profit_factor | 0.4100 |
| gross_win_rate | 0.3114 |
| sharpe_ratio | -8.5118 |
| sortino_ratio | -2.4456 |
| max_drawdown | 0.9622 |
| cagr | -0.7271 |
| net_avg_win | 16.0880 |
| net_avg_loss | -39.3184 |
| avg_hold_time_bars | 28.6983 |
| exposure | 0.5338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
