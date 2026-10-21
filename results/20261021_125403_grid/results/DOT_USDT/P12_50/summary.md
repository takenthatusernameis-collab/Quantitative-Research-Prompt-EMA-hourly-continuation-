# EMA Hourly Continuation — DOT/USDT P12_50

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.7725 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0189 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -1.8619 |
| sortino_ratio | -0.6300 |
| max_drawdown | 0.5623 |
| cagr | -0.2510 |
| net_avg_win | 62.3519 |
| net_avg_loss | -82.7772 |
| avg_hold_time_bars | 14.1964 |
| exposure | 0.3581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
