# EMA Hourly Continuation — ONDO/USDT P8_55

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1090 |
| net_profit_factor | 0.6103 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9345 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -5.4753 |
| sortino_ratio | -2.5283 |
| max_drawdown | 0.9568 |
| cagr | -0.7084 |
| net_avg_win | 28.7468 |
| net_avg_loss | -42.9744 |
| avg_hold_time_bars | 9.2018 |
| exposure | 0.4559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
