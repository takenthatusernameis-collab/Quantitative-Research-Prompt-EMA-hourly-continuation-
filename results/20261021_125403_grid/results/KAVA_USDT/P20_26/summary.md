# EMA Hourly Continuation — KAVA/USDT P20_26

**Symbol:** KAVA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.5339 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.9482 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -3.5233 |
| sortino_ratio | -0.8218 |
| max_drawdown | 0.6343 |
| cagr | -0.3194 |
| net_avg_win | 58.1812 |
| net_avg_loss | -94.2818 |
| avg_hold_time_bars | 6.0951 |
| exposure | 0.0729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
