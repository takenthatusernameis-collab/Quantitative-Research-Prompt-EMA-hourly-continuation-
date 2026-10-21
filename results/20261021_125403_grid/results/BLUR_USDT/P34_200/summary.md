# EMA Hourly Continuation — BLUR/USDT P34_200

**Symbol:** BLUR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 1.0570 |
| net_win_rate | 0.5580 |
| gross_profit_factor | 1.2444 |
| gross_win_rate | 0.5580 |
| sharpe_ratio | 0.3339 |
| sortino_ratio | 0.0804 |
| max_drawdown | 0.1070 |
| cagr | 0.0299 |
| net_avg_win | 92.7456 |
| net_avg_loss | -110.7541 |
| avg_hold_time_bars | 45.1196 |
| exposure | 0.5635 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
