# EMA Hourly Continuation — NEAR/USDT P12_50

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.7882 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 0.9742 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -1.8206 |
| sortino_ratio | -0.6321 |
| max_drawdown | 0.5281 |
| cagr | -0.2534 |
| net_avg_win | 66.5149 |
| net_avg_loss | -82.4024 |
| avg_hold_time_bars | 11.6265 |
| exposure | 0.3113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
