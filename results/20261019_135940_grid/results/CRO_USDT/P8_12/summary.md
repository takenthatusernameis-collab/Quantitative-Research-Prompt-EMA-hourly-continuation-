# EMA Hourly Continuation — CRO/USDT P8_12

**Symbol:** CRO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1894 |
| net_profit_factor | 0.1096 |
| net_win_rate | 0.3094 |
| gross_profit_factor | 0.5556 |
| gross_win_rate | 0.4013 |
| sharpe_ratio | -21.8769 |
| sortino_ratio | -14.2686 |
| max_drawdown | 1.0000 |
| cagr | -0.9996 |
| net_avg_win | 2.1011 |
| net_avg_loss | -8.5866 |
| avg_hold_time_bars | 1.8970 |
| exposure | 0.1633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
