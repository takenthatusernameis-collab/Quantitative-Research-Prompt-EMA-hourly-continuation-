# EMA Hourly Continuation — LDO/USDT P50_200

**Symbol:** LDO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.7615 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.8965 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -1.3640 |
| sortino_ratio | -0.3268 |
| max_drawdown | 0.3520 |
| cagr | -0.1404 |
| net_avg_win | 74.1839 |
| net_avg_loss | -89.5217 |
| avg_hold_time_bars | 31.4754 |
| exposure | 0.4063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
