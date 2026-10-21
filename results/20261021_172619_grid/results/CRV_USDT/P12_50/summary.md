# EMA Hourly Continuation — CRV/USDT P12_50

**Symbol:** CRV/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.7812 |
| net_win_rate | 0.4992 |
| gross_profit_factor | 0.9805 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -1.8152 |
| sortino_ratio | -0.6386 |
| max_drawdown | 0.5431 |
| cagr | -0.2547 |
| net_avg_win | 61.9252 |
| net_avg_loss | -79.0070 |
| avg_hold_time_bars | 11.0000 |
| exposure | 0.3015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
