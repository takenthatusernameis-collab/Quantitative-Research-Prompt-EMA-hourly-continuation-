# EMA Hourly Continuation — BONK/USDT P12_200

**Symbol:** BONK/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 1.0182 |
| net_win_rate | 0.5391 |
| gross_profit_factor | 1.1644 |
| gross_win_rate | 0.5430 |
| sharpe_ratio | 0.1431 |
| sortino_ratio | 0.0331 |
| max_drawdown | 0.2230 |
| cagr | 0.0094 |
| net_avg_win | 96.4966 |
| net_avg_loss | -110.8380 |
| avg_hold_time_bars | 64.8867 |
| exposure | 0.7550 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
