# EMA Hourly Continuation — XLM/USDT P50_100

**Symbol:** XLM/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.4191 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 1.0080 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -5.5653 |
| sortino_ratio | -1.9247 |
| max_drawdown | 0.9156 |
| cagr | -0.6209 |
| net_avg_win | 22.7026 |
| net_avg_loss | -49.2424 |
| avg_hold_time_bars | 6.3974 |
| exposure | 0.1771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
