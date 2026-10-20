# EMA Hourly Continuation — IOST/USDT P8_12

**Symbol:** IOST/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1715 |
| net_profit_factor | 0.1652 |
| net_win_rate | 0.3726 |
| gross_profit_factor | 0.7085 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -17.3241 |
| sortino_ratio | -10.4216 |
| max_drawdown | 1.0000 |
| cagr | -0.9964 |
| net_avg_win | 3.0979 |
| net_avg_loss | -11.1334 |
| avg_hold_time_bars | 2.3883 |
| exposure | 0.1862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
