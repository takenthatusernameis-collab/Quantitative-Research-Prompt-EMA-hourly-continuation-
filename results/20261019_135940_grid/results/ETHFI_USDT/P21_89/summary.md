# EMA Hourly Continuation — ETHFI/USDT P21_89

**Symbol:** ETHFI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 748 |
| net_profit_factor | 0.6402 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9536 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -3.9410 |
| sortino_ratio | -1.5122 |
| max_drawdown | 0.8399 |
| cagr | -0.5179 |
| net_avg_win | 41.9786 |
| net_avg_loss | -59.5499 |
| avg_hold_time_bars | 11.2674 |
| exposure | 0.3831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
