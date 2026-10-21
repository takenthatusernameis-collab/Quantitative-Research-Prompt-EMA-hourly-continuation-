# EMA Hourly Continuation — LDO/USDT P12_55

**Symbol:** LDO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.7461 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9211 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -2.1453 |
| sortino_ratio | -0.7565 |
| max_drawdown | 0.5914 |
| cagr | -0.2938 |
| net_avg_win | 57.8459 |
| net_avg_loss | -73.0845 |
| avg_hold_time_bars | 12.5443 |
| exposure | 0.3478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
