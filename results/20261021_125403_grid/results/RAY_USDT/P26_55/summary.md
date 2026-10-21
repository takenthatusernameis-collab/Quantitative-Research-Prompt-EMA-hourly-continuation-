# EMA Hourly Continuation — RAY/USDT P26_55

**Symbol:** RAY/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.8664 |
| net_win_rate | 0.5335 |
| gross_profit_factor | 1.1417 |
| gross_win_rate | 0.5335 |
| sharpe_ratio | -0.9997 |
| sortino_ratio | -0.3053 |
| max_drawdown | 0.4502 |
| cagr | -0.1334 |
| net_avg_win | 81.9800 |
| net_avg_loss | -108.2003 |
| avg_hold_time_bars | 6.7143 |
| exposure | 0.1367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
