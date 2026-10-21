# EMA Hourly Continuation — ENA/USDT P89_144

**Symbol:** ENA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 204 |
| net_profit_factor | 1.0054 |
| net_win_rate | 0.5539 |
| gross_profit_factor | 1.2294 |
| gross_win_rate | 0.5539 |
| sharpe_ratio | 0.0686 |
| sortino_ratio | 0.0142 |
| max_drawdown | 0.1389 |
| cagr | 0.0021 |
| net_avg_win | 88.5022 |
| net_avg_loss | -109.3111 |
| avg_hold_time_bars | 8.0441 |
| exposure | 0.0746 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
