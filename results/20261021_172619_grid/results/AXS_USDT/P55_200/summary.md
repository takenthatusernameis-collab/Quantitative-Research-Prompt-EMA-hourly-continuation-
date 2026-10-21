# EMA Hourly Continuation — AXS/USDT P55_200

**Symbol:** AXS/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 1.0057 |
| net_win_rate | 0.5581 |
| gross_profit_factor | 1.2511 |
| gross_win_rate | 0.5581 |
| sharpe_ratio | 0.0798 |
| sortino_ratio | 0.0189 |
| max_drawdown | 0.1295 |
| cagr | 0.0029 |
| net_avg_win | 87.7499 |
| net_avg_loss | -110.1755 |
| avg_hold_time_bars | 28.3184 |
| exposure | 0.3421 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
