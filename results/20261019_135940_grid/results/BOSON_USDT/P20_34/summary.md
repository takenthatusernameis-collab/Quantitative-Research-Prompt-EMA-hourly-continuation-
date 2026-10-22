# EMA Hourly Continuation — BOSON/USDT P20_34

**Symbol:** BOSON/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 994 |
| net_profit_factor | 0.4669 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8727 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -7.3831 |
| sortino_ratio | -3.2743 |
| max_drawdown | 0.9824 |
| cagr | -0.7984 |
| net_avg_win | 19.5474 |
| net_avg_loss | -33.2519 |
| avg_hold_time_bars | 3.7817 |
| exposure | 0.1709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
