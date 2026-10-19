# EMA Hourly Continuation — JASMY/USDT P20_200

**Symbol:** JASMY/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 1.0097 |
| net_win_rate | 0.5779 |
| gross_profit_factor | 1.4115 |
| gross_win_rate | 0.5864 |
| sharpe_ratio | 0.1189 |
| sortino_ratio | 0.0321 |
| max_drawdown | 0.2179 |
| cagr | 0.0071 |
| net_avg_win | 91.4789 |
| net_avg_loss | -124.0449 |
| avg_hold_time_bars | 40.8952 |
| exposure | 0.6562 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
