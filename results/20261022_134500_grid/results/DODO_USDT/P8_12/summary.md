# EMA Hourly Continuation — DODO/USDT P8_12

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1898 |
| net_profit_factor | 0.2099 |
| net_win_rate | 0.3809 |
| gross_profit_factor | 0.7165 |
| gross_win_rate | 0.4305 |
| sharpe_ratio | -16.5038 |
| sortino_ratio | -10.2389 |
| max_drawdown | 1.0000 |
| cagr | -0.9952 |
| net_avg_win | 3.6736 |
| net_avg_loss | -10.7710 |
| avg_hold_time_bars | 2.1691 |
| exposure | 0.1863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
