# EMA Hourly Continuation — EWT/USDT P12_34

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.5762 |
| net_win_rate | 0.4328 |
| gross_profit_factor | 0.7618 |
| gross_win_rate | 0.4328 |
| sharpe_ratio | -3.6628 |
| sortino_ratio | -1.0892 |
| max_drawdown | 0.7166 |
| cagr | -0.3947 |
| net_avg_win | 51.2837 |
| net_avg_loss | -67.9113 |
| avg_hold_time_bars | 8.0091 |
| exposure | 0.1598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
