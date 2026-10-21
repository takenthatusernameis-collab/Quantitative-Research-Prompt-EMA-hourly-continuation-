# EMA Hourly Continuation — ONT/USDT P8_20

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.6630 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9767 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -3.1334 |
| sortino_ratio | -1.0932 |
| max_drawdown | 0.7284 |
| cagr | -0.3930 |
| net_avg_win | 47.9105 |
| net_avg_loss | -71.0597 |
| avg_hold_time_bars | 5.4351 |
| exposure | 0.1458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
