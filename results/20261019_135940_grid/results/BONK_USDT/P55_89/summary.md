# EMA Hourly Continuation — BONK/USDT P55_89

**Symbol:** BONK/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.5627 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.9432 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -5.1334 |
| sortino_ratio | -1.8774 |
| max_drawdown | 0.9106 |
| cagr | -0.6068 |
| net_avg_win | 36.0189 |
| net_avg_loss | -56.9549 |
| avg_hold_time_bars | 3.8790 |
| exposure | 0.1210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
