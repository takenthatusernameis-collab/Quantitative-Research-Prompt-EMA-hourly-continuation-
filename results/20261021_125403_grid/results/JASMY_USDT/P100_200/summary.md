# EMA Hourly Continuation — JASMY/USDT P100_200

**Symbol:** JASMY/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 243 |
| net_profit_factor | 1.0146 |
| net_win_rate | 0.5597 |
| gross_profit_factor | 1.2620 |
| gross_win_rate | 0.5597 |
| sharpe_ratio | 0.1143 |
| sortino_ratio | 0.0260 |
| max_drawdown | 0.2067 |
| cagr | 0.0064 |
| net_avg_win | 82.6387 |
| net_avg_loss | -103.5225 |
| avg_hold_time_bars | 16.1317 |
| exposure | 0.1782 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
