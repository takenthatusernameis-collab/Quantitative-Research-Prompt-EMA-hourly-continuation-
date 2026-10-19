# EMA Hourly Continuation — SUN/USDT P8_100

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.4649 |
| net_win_rate | 0.4153 |
| gross_profit_factor | 0.8935 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -7.1760 |
| sortino_ratio | -2.5130 |
| max_drawdown | 0.9640 |
| cagr | -0.7251 |
| net_avg_win | 32.1334 |
| net_avg_loss | -49.0981 |
| avg_hold_time_bars | 23.5367 |
| exposure | 0.6668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
