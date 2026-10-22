# EMA Hourly Continuation — PEOPLE/USDT P21_144

**Symbol:** PEOPLE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 1.0698 |
| net_win_rate | 0.5573 |
| gross_profit_factor | 1.2517 |
| gross_win_rate | 0.5573 |
| sharpe_ratio | 0.4303 |
| sortino_ratio | 0.1125 |
| max_drawdown | 0.1362 |
| cagr | 0.0429 |
| net_avg_win | 95.2044 |
| net_avg_loss | -112.0204 |
| avg_hold_time_bars | 39.3158 |
| exposure | 0.5746 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
