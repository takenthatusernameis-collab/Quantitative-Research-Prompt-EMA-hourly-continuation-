# EMA Hourly Continuation — WLD/USDT P26_34

**Symbol:** WLD/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1041 |
| net_profit_factor | 0.3668 |
| net_win_rate | 0.4304 |
| gross_profit_factor | 0.8041 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -9.9526 |
| sortino_ratio | -4.5451 |
| max_drawdown | 0.9974 |
| cagr | -0.9058 |
| net_avg_win | 12.8984 |
| net_avg_loss | -26.5632 |
| avg_hold_time_bars | 1.9289 |
| exposure | 0.0913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
