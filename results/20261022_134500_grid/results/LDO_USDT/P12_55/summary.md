# EMA Hourly Continuation — LDO/USDT P12_55

**Symbol:** LDO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1027 |
| net_profit_factor | 0.5246 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8595 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -6.3128 |
| sortino_ratio | -2.8172 |
| max_drawdown | 0.9702 |
| cagr | -0.7517 |
| net_avg_win | 22.7723 |
| net_avg_loss | -36.6256 |
| avg_hold_time_bars | 8.1217 |
| exposure | 0.3791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
