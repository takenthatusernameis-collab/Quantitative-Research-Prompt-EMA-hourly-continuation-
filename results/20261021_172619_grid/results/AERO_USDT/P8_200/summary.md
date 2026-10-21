# EMA Hourly Continuation — AERO/USDT P8_200

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 1.1594 |
| net_win_rate | 0.5668 |
| gross_profit_factor | 1.2858 |
| gross_win_rate | 0.5668 |
| sharpe_ratio | 0.8407 |
| sortino_ratio | 0.1935 |
| max_drawdown | 0.1298 |
| cagr | 0.0814 |
| net_avg_win | 112.8470 |
| net_avg_loss | -127.3482 |
| avg_hold_time_bars | 72.1336 |
| exposure | 0.8099 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
