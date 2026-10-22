# EMA Hourly Continuation — DOGE/USDT P12_200

**Symbol:** DOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.6829 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0560 |
| gross_win_rate | 0.5118 |
| sharpe_ratio | -2.3918 |
| sortino_ratio | -0.6160 |
| max_drawdown | 0.5365 |
| cagr | -0.2587 |
| net_avg_win | 66.5525 |
| net_avg_loss | -98.6140 |
| avg_hold_time_bars | 49.0647 |
| exposure | 0.7583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
