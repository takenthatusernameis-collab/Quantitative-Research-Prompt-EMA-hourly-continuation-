# EMA Hourly Continuation — MEW/USDT P8_21

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1593 |
| net_profit_factor | 0.5832 |
| net_win_rate | 0.4350 |
| gross_profit_factor | 0.9704 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -10.2401 |
| sortino_ratio | -5.7369 |
| max_drawdown | 0.9993 |
| cagr | -0.9423 |
| net_avg_win | 20.1760 |
| net_avg_loss | -26.6380 |
| avg_hold_time_bars | 3.0973 |
| exposure | 0.2243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
