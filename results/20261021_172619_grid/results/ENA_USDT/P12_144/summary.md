# EMA Hourly Continuation — ENA/USDT P12_144

**Symbol:** ENA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 1.0155 |
| net_win_rate | 0.5351 |
| gross_profit_factor | 1.1451 |
| gross_win_rate | 0.5351 |
| sharpe_ratio | 0.1535 |
| sortino_ratio | 0.0427 |
| max_drawdown | 0.1502 |
| cagr | 0.0113 |
| net_avg_win | 94.5691 |
| net_avg_loss | -107.1981 |
| avg_hold_time_bars | 38.0730 |
| exposure | 0.6403 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
