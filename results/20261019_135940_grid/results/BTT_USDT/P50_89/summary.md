# EMA Hourly Continuation — BTT/USDT P50_89

**Symbol:** BTT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.2476 |
| net_win_rate | 0.3124 |
| gross_profit_factor | 0.6461 |
| gross_win_rate | 0.3854 |
| sharpe_ratio | -12.1741 |
| sortino_ratio | -4.7532 |
| max_drawdown | 0.9984 |
| cagr | -0.9235 |
| net_avg_win | 15.3556 |
| net_avg_loss | -28.1748 |
| avg_hold_time_bars | 5.2949 |
| exposure | 0.1649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
