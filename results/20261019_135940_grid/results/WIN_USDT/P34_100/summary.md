# EMA Hourly Continuation — WIN/USDT P34_100

**Symbol:** WIN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.4198 |
| net_win_rate | 0.4337 |
| gross_profit_factor | 0.8240 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -6.3493 |
| sortino_ratio | -2.1689 |
| max_drawdown | 0.9366 |
| cagr | -0.6632 |
| net_avg_win | 26.5270 |
| net_avg_loss | -48.3907 |
| avg_hold_time_bars | 10.5901 |
| exposure | 0.2830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
