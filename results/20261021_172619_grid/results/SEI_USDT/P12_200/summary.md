# EMA Hourly Continuation — SEI/USDT P12_200

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 195 |
| net_profit_factor | 1.0211 |
| net_win_rate | 0.5436 |
| gross_profit_factor | 1.1724 |
| gross_win_rate | 0.5436 |
| sharpe_ratio | 0.1369 |
| sortino_ratio | 0.0276 |
| max_drawdown | 0.1273 |
| cagr | 0.0082 |
| net_avg_win | 94.7548 |
| net_avg_loss | -110.5239 |
| avg_hold_time_bars | 92.0410 |
| exposure | 0.8158 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
