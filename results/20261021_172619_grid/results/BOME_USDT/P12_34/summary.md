# EMA Hourly Continuation — BOME/USDT P12_34

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.7508 |
| net_win_rate | 0.4860 |
| gross_profit_factor | 0.9414 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -2.2617 |
| sortino_ratio | -0.7976 |
| max_drawdown | 0.6411 |
| cagr | -0.3075 |
| net_avg_win | 61.3481 |
| net_avg_loss | -77.2677 |
| avg_hold_time_bars | 5.6798 |
| exposure | 0.1572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
