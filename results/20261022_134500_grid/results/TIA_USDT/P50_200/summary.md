# EMA Hourly Continuation — TIA/USDT P50_200

**Symbol:** TIA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.8251 |
| net_win_rate | 0.5183 |
| gross_profit_factor | 1.0719 |
| gross_win_rate | 0.5183 |
| sharpe_ratio | -1.0884 |
| sortino_ratio | -0.2801 |
| max_drawdown | 0.3080 |
| cagr | -0.1251 |
| net_avg_win | 79.0857 |
| net_avg_loss | -103.1349 |
| avg_hold_time_bars | 28.4451 |
| exposure | 0.4241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
