# EMA Hourly Continuation — XMR/USDT P34_200

**Symbol:** XMR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.4898 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.8456 |
| gross_win_rate | 0.4475 |
| sharpe_ratio | -5.5553 |
| sortino_ratio | -1.9567 |
| max_drawdown | 0.9151 |
| cagr | -0.6188 |
| net_avg_win | 31.2422 |
| net_avg_loss | -51.3227 |
| avg_hold_time_bars | 15.6799 |
| exposure | 0.4476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
