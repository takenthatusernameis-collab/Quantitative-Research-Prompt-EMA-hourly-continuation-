# EMA Hourly Continuation — SKL/USDT P34_50

**Symbol:** SKL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 967 |
| net_profit_factor | 0.4168 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.8966 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -8.4696 |
| sortino_ratio | -3.7454 |
| max_drawdown | 0.9903 |
| cagr | -0.8404 |
| net_avg_win | 16.3800 |
| net_avg_loss | -31.7317 |
| avg_hold_time_bars | 2.8407 |
| exposure | 0.1249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
