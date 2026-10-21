# EMA Hourly Continuation — ETHFI/USDT P55_200

**Symbol:** ETHFI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 1.0235 |
| net_win_rate | 0.5488 |
| gross_profit_factor | 1.2027 |
| gross_win_rate | 0.5488 |
| sharpe_ratio | 0.1905 |
| sortino_ratio | 0.0477 |
| max_drawdown | 0.1478 |
| cagr | 0.0149 |
| net_avg_win | 101.3170 |
| net_avg_loss | -120.4185 |
| avg_hold_time_bars | 26.1279 |
| exposure | 0.3527 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
