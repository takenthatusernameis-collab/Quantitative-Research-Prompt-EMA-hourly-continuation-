# EMA Hourly Continuation — SUI/USDT P89_200

**Symbol:** SUI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.5279 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.8322 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -4.1049 |
| sortino_ratio | -1.1559 |
| max_drawdown | 0.7726 |
| cagr | -0.4361 |
| net_avg_win | 46.6060 |
| net_avg_loss | -71.8073 |
| avg_hold_time_bars | 9.4975 |
| exposure | 0.1761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
