# EMA Hourly Continuation — WLD/USDT P8_144

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 1.0382 |
| net_win_rate | 0.5422 |
| gross_profit_factor | 1.1719 |
| gross_win_rate | 0.5422 |
| sharpe_ratio | 0.2898 |
| sortino_ratio | 0.0805 |
| max_drawdown | 0.1269 |
| cagr | 0.0281 |
| net_avg_win | 98.5120 |
| net_avg_loss | -112.4003 |
| avg_hold_time_bars | 43.4196 |
| exposure | 0.7243 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
