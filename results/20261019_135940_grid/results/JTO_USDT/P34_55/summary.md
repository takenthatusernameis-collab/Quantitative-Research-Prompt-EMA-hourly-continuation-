# EMA Hourly Continuation — JTO/USDT P34_55

**Symbol:** JTO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 871 |
| net_profit_factor | 0.4778 |
| net_win_rate | 0.4363 |
| gross_profit_factor | 0.8604 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -6.9421 |
| sortino_ratio | -2.8980 |
| max_drawdown | 0.9707 |
| cagr | -0.7532 |
| net_avg_win | 23.3652 |
| net_avg_loss | -37.8430 |
| avg_hold_time_bars | 3.6866 |
| exposure | 0.1460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
