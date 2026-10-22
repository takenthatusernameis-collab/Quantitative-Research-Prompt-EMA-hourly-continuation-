# EMA Hourly Continuation — GRAM/USDT P8_55

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1086 |
| net_profit_factor | 0.4861 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.9482 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -8.3479 |
| sortino_ratio | -3.8475 |
| max_drawdown | 0.9928 |
| cagr | -0.8566 |
| net_avg_win | 19.5967 |
| net_avg_loss | -31.8133 |
| avg_hold_time_bars | 9.8766 |
| exposure | 0.4875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
