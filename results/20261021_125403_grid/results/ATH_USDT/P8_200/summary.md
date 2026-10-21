# EMA Hourly Continuation — ATH/USDT P8_200

**Symbol:** ATH/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 1.0638 |
| net_win_rate | 0.5521 |
| gross_profit_factor | 1.2135 |
| gross_win_rate | 0.5521 |
| sharpe_ratio | 0.3819 |
| sortino_ratio | 0.0921 |
| max_drawdown | 0.1004 |
| cagr | 0.0351 |
| net_avg_win | 98.5732 |
| net_avg_loss | -114.2292 |
| avg_hold_time_bars | 63.8301 |
| exposure | 0.8013 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
