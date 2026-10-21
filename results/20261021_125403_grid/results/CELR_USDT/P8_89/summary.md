# EMA Hourly Continuation — CELR/USDT P8_89

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.7618 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.9442 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -2.1442 |
| sortino_ratio | -0.7069 |
| max_drawdown | 0.5652 |
| cagr | -0.2783 |
| net_avg_win | 69.2454 |
| net_avg_loss | -84.6863 |
| avg_hold_time_bars | 26.2886 |
| exposure | 0.6388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
