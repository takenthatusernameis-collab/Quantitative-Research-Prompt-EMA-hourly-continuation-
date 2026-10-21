# EMA Hourly Continuation — APT/USDT P21_144

**Symbol:** APT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 1.0362 |
| net_win_rate | 0.5522 |
| gross_profit_factor | 1.2175 |
| gross_win_rate | 0.5522 |
| sharpe_ratio | 0.2367 |
| sortino_ratio | 0.0592 |
| max_drawdown | 0.1250 |
| cagr | 0.0200 |
| net_avg_win | 89.0311 |
| net_avg_loss | -105.9495 |
| avg_hold_time_bars | 43.5758 |
| exposure | 0.5883 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
