# EMA Hourly Continuation — LDO/USDT P12_200

**Symbol:** LDO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.6139 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.7958 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -2.3969 |
| sortino_ratio | -0.5735 |
| max_drawdown | 0.5308 |
| cagr | -0.2372 |
| net_avg_win | 59.8763 |
| net_avg_loss | -79.8625 |
| avg_hold_time_bars | 59.0069 |
| exposure | 0.7805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
