# EMA Hourly Continuation — ELON/USDT P8_21

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1563 |
| net_profit_factor | 0.3430 |
| net_win_rate | 0.4274 |
| gross_profit_factor | 0.7557 |
| gross_win_rate | 0.4402 |
| sharpe_ratio | -11.6833 |
| sortino_ratio | -6.5816 |
| max_drawdown | 0.9997 |
| cagr | -0.9609 |
| net_avg_win | 7.8147 |
| net_avg_loss | -17.0026 |
| avg_hold_time_bars | 3.1318 |
| exposure | 0.2225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
