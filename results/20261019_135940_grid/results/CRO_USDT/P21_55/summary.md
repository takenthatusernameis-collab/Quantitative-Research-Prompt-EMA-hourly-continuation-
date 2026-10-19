# EMA Hourly Continuation — CRO/USDT P21_55

**Symbol:** CRO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 979 |
| net_profit_factor | 0.3522 |
| net_win_rate | 0.4147 |
| gross_profit_factor | 0.8016 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -9.4538 |
| sortino_ratio | -4.1694 |
| max_drawdown | 0.9954 |
| cagr | -0.8800 |
| net_avg_win | 13.3255 |
| net_avg_loss | -26.8089 |
| avg_hold_time_bars | 5.5986 |
| exposure | 0.2491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
