# EMA Hourly Continuation — IOST/USDT P100_144

**Symbol:** IOST/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.4207 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.8944 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -5.3917 |
| sortino_ratio | -1.7111 |
| max_drawdown | 0.8841 |
| cagr | -0.5719 |
| net_avg_win | 27.5846 |
| net_avg_loss | -56.5489 |
| avg_hold_time_bars | 4.1936 |
| exposure | 0.0955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
