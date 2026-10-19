# EMA Hourly Continuation — JTO/USDT P8_55

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1003 |
| net_profit_factor | 0.6054 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.8814 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -5.6580 |
| sortino_ratio | -2.5103 |
| max_drawdown | 0.9562 |
| cagr | -0.7024 |
| net_avg_win | 32.3897 |
| net_avg_loss | -43.7156 |
| avg_hold_time_bars | 11.3180 |
| exposure | 0.5160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
