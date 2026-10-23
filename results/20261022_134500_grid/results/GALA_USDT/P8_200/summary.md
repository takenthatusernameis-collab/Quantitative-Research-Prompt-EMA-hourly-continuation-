# EMA Hourly Continuation — GALA/USDT P8_200

**Symbol:** GALA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.7048 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9434 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -1.7854 |
| sortino_ratio | -0.4478 |
| max_drawdown | 0.4246 |
| cagr | -0.1917 |
| net_avg_win | 63.7911 |
| net_avg_loss | -86.0618 |
| avg_hold_time_bars | 56.8962 |
| exposure | 0.8224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
