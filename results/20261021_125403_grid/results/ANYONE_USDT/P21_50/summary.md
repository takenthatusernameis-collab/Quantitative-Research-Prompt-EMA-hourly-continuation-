# EMA Hourly Continuation — ANYONE/USDT P21_50

**Symbol:** ANYONE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.6202 |
| net_win_rate | 0.4302 |
| gross_profit_factor | 0.7503 |
| gross_win_rate | 0.4302 |
| sharpe_ratio | -3.4242 |
| sortino_ratio | -1.0825 |
| max_drawdown | 0.6874 |
| cagr | -0.3937 |
| net_avg_win | 56.9853 |
| net_avg_loss | -69.3627 |
| avg_hold_time_bars | 7.4013 |
| exposure | 0.1687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
