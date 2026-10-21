# EMA Hourly Continuation — JASMY/USDT P8_144

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 1.0006 |
| net_win_rate | 0.5423 |
| gross_profit_factor | 1.1767 |
| gross_win_rate | 0.5423 |
| sharpe_ratio | 0.0618 |
| sortino_ratio | 0.0166 |
| max_drawdown | 0.2301 |
| cagr | 0.0004 |
| net_avg_win | 95.9521 |
| net_avg_loss | -113.6111 |
| avg_hold_time_bars | 48.1108 |
| exposure | 0.7501 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
