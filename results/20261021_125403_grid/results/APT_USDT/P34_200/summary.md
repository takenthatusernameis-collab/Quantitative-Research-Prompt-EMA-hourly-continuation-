# EMA Hourly Continuation — APT/USDT P34_200

**Symbol:** APT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 1.0818 |
| net_win_rate | 0.5620 |
| gross_profit_factor | 1.2654 |
| gross_win_rate | 0.5620 |
| sharpe_ratio | 0.4327 |
| sortino_ratio | 0.0980 |
| max_drawdown | 0.1297 |
| cagr | 0.0383 |
| net_avg_win | 96.2141 |
| net_avg_loss | -114.1123 |
| avg_hold_time_bars | 51.4050 |
| exposure | 0.5655 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
