# EMA Hourly Continuation — WLD/USDT P8_21

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.9988 |
| net_win_rate | 0.5648 |
| gross_profit_factor | 1.2813 |
| gross_win_rate | 0.5648 |
| sharpe_ratio | 0.0604 |
| sortino_ratio | 0.0191 |
| max_drawdown | 0.1812 |
| cagr | -0.0010 |
| net_avg_win | 85.3928 |
| net_avg_loss | -110.9304 |
| avg_hold_time_bars | 5.4607 |
| exposure | 0.1169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
