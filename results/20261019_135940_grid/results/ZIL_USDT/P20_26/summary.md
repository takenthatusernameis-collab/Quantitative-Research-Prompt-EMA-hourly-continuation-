# EMA Hourly Continuation — ZIL/USDT P20_26

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1257 |
| net_profit_factor | 0.1843 |
| net_win_rate | 0.3365 |
| gross_profit_factor | 0.7218 |
| gross_win_rate | 0.3994 |
| sharpe_ratio | -15.7830 |
| sortino_ratio | -8.2104 |
| max_drawdown | 1.0000 |
| cagr | -0.9878 |
| net_avg_win | 5.3430 |
| net_avg_loss | -14.7002 |
| avg_hold_time_bars | 1.9356 |
| exposure | 0.1106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
