# EMA Hourly Continuation — CSPR/USDT P34_144

**Symbol:** CSPR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.6687 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.8306 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -2.6228 |
| sortino_ratio | -0.7800 |
| max_drawdown | 0.6016 |
| cagr | -0.3018 |
| net_avg_win | 60.2660 |
| net_avg_loss | -74.4215 |
| avg_hold_time_bars | 18.6886 |
| exposure | 0.3738 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
