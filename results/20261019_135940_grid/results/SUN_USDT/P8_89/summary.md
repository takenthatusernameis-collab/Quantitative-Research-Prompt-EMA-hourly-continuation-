# EMA Hourly Continuation — SUN/USDT P8_89

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.4279 |
| net_win_rate | 0.4084 |
| gross_profit_factor | 0.8220 |
| gross_win_rate | 0.4329 |
| sharpe_ratio | -7.8356 |
| sortino_ratio | -2.8782 |
| max_drawdown | 0.9786 |
| cagr | -0.7765 |
| net_avg_win | 25.8291 |
| net_avg_loss | -41.6618 |
| avg_hold_time_bars | 19.7547 |
| exposure | 0.6195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
