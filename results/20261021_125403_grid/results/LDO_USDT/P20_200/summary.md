# EMA Hourly Continuation — LDO/USDT P20_200

**Symbol:** LDO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.7232 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.8343 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -1.6338 |
| sortino_ratio | -0.3868 |
| max_drawdown | 0.4008 |
| cagr | -0.1640 |
| net_avg_win | 73.3801 |
| net_avg_loss | -86.6823 |
| avg_hold_time_bars | 50.4179 |
| exposure | 0.6417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
