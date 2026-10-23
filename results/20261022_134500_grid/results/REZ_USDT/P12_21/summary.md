# EMA Hourly Continuation — REZ/USDT P12_21

**Symbol:** REZ/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1364 |
| net_profit_factor | 0.4568 |
| net_win_rate | 0.4260 |
| gross_profit_factor | 0.8728 |
| gross_win_rate | 0.4443 |
| sharpe_ratio | -10.2917 |
| sortino_ratio | -5.4007 |
| max_drawdown | 0.9987 |
| cagr | -0.9323 |
| net_avg_win | 14.4536 |
| net_avg_loss | -23.4799 |
| avg_hold_time_bars | 2.7412 |
| exposure | 0.1725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
