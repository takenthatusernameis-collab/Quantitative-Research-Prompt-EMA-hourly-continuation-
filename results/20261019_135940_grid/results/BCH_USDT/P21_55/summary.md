# EMA Hourly Continuation — BCH/USDT P21_55

**Symbol:** BCH/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.3413 |
| net_win_rate | 0.4199 |
| gross_profit_factor | 0.7347 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -9.2678 |
| sortino_ratio | -4.0018 |
| max_drawdown | 0.9935 |
| cagr | -0.8649 |
| net_avg_win | 13.2690 |
| net_avg_loss | -28.1396 |
| avg_hold_time_bars | 5.5963 |
| exposure | 0.2350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
