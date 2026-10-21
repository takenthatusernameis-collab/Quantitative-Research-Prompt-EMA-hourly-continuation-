# EMA Hourly Continuation — LSK/USDT P20_144

**Symbol:** LSK/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.8052 |
| net_win_rate | 0.5062 |
| gross_profit_factor | 1.0207 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -1.3207 |
| sortino_ratio | -0.3785 |
| max_drawdown | 0.4127 |
| cagr | -0.1614 |
| net_avg_win | 72.7662 |
| net_avg_loss | -92.6489 |
| avg_hold_time_bars | 28.8479 |
| exposure | 0.5258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
