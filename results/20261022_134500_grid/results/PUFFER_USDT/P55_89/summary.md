# EMA Hourly Continuation — PUFFER/USDT P55_89

**Symbol:** PUFFER/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.4934 |
| net_win_rate | 0.4363 |
| gross_profit_factor | 0.8032 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -5.4264 |
| sortino_ratio | -1.9172 |
| max_drawdown | 0.8457 |
| cagr | -0.5989 |
| net_avg_win | 37.4286 |
| net_avg_loss | -58.7024 |
| avg_hold_time_bars | 5.5618 |
| exposure | 0.1580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
