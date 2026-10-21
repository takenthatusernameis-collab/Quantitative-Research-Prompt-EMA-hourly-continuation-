# EMA Hourly Continuation — BRETT/USDT P89_200

**Symbol:** BRETT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.8312 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 0.9808 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.8902 |
| sortino_ratio | -0.2037 |
| max_drawdown | 0.2596 |
| cagr | -0.0909 |
| net_avg_win | 83.0112 |
| net_avg_loss | -98.2301 |
| avg_hold_time_bars | 17.7851 |
| exposure | 0.2071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
