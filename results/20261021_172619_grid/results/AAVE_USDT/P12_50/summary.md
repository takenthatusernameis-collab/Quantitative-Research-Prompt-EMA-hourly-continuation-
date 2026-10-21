# EMA Hourly Continuation — AAVE/USDT P12_50

**Symbol:** AAVE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.7042 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 0.8986 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -2.8185 |
| sortino_ratio | -0.9678 |
| max_drawdown | 0.6822 |
| cagr | -0.3586 |
| net_avg_win | 58.8181 |
| net_avg_loss | -73.5265 |
| avg_hold_time_bars | 11.6919 |
| exposure | 0.3088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
