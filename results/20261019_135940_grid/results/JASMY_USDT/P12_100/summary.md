# EMA Hourly Continuation — JASMY/USDT P12_100

**Symbol:** JASMY/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.6527 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9258 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -3.2256 |
| sortino_ratio | -1.1515 |
| max_drawdown | 0.7656 |
| cagr | -0.4236 |
| net_avg_win | 44.9932 |
| net_avg_loss | -65.3829 |
| avg_hold_time_bars | 19.6719 |
| exposure | 0.5750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
