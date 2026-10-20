# EMA Hourly Continuation — ZIL/USDT P50_100

**Symbol:** ZIL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.5226 |
| net_win_rate | 0.4566 |
| gross_profit_factor | 0.9390 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -5.5193 |
| sortino_ratio | -2.0218 |
| max_drawdown | 0.9145 |
| cagr | -0.6203 |
| net_avg_win | 32.7358 |
| net_avg_loss | -52.6327 |
| avg_hold_time_bars | 6.0359 |
| exposure | 0.1833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
