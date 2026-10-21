# EMA Hourly Continuation — BONK/USDT P8_200

**Symbol:** BONK/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 1.0186 |
| net_win_rate | 0.5430 |
| gross_profit_factor | 1.1673 |
| gross_win_rate | 0.5430 |
| sharpe_ratio | 0.1472 |
| sortino_ratio | 0.0340 |
| max_drawdown | 0.2373 |
| cagr | 0.0098 |
| net_avg_win | 97.8497 |
| net_avg_loss | -114.1266 |
| avg_hold_time_bars | 68.3477 |
| exposure | 0.7953 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
