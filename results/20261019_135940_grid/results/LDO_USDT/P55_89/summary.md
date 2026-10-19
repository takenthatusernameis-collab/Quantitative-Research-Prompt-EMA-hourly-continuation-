# EMA Hourly Continuation — LDO/USDT P55_89

**Symbol:** LDO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 722 |
| net_profit_factor | 0.4739 |
| net_win_rate | 0.4280 |
| gross_profit_factor | 0.7727 |
| gross_win_rate | 0.4391 |
| sharpe_ratio | -6.5172 |
| sortino_ratio | -2.4695 |
| max_drawdown | 0.9520 |
| cagr | -0.7002 |
| net_avg_win | 27.7344 |
| net_avg_loss | -43.7882 |
| avg_hold_time_bars | 3.9460 |
| exposure | 0.1295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
