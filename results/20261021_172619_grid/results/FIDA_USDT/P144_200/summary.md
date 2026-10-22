# EMA Hourly Continuation — FIDA/USDT P144_200

**Symbol:** FIDA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.5042 |
| net_win_rate | 0.4228 |
| gross_profit_factor | 0.7125 |
| gross_win_rate | 0.4228 |
| sharpe_ratio | -3.1726 |
| sortino_ratio | -0.7061 |
| max_drawdown | 0.5641 |
| cagr | -0.2783 |
| net_avg_win | 54.8353 |
| net_avg_loss | -79.6513 |
| avg_hold_time_bars | 7.9553 |
| exposure | 0.0886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
