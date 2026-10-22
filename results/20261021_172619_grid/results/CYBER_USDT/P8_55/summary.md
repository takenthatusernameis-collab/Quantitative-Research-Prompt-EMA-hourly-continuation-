# EMA Hourly Continuation — CYBER/USDT P8_55

**Symbol:** CYBER/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 744 |
| net_profit_factor | 0.7388 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9345 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -2.7573 |
| sortino_ratio | -1.0728 |
| max_drawdown | 0.7154 |
| cagr | -0.3900 |
| net_avg_win | 56.0282 |
| net_avg_loss | -70.7113 |
| avg_hold_time_bars | 14.0995 |
| exposure | 0.4768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
