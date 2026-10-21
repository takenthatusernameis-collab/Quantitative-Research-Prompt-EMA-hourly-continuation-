# EMA Hourly Continuation — POPCAT/USDT P8_200

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 1.0255 |
| net_win_rate | 0.5448 |
| gross_profit_factor | 1.1761 |
| gross_win_rate | 0.5448 |
| sharpe_ratio | 0.2106 |
| sortino_ratio | 0.0537 |
| max_drawdown | 0.1708 |
| cagr | 0.0174 |
| net_avg_win | 104.6048 |
| net_avg_loss | -122.0671 |
| avg_hold_time_bars | 55.6754 |
| exposure | 0.7882 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
