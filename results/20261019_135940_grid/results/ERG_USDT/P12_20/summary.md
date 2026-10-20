# EMA Hourly Continuation — ERG/USDT P12_20

**Symbol:** ERG/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1505 |
| net_profit_factor | 0.1502 |
| net_win_rate | 0.2731 |
| gross_profit_factor | 0.4065 |
| gross_win_rate | 0.3103 |
| sharpe_ratio | -19.2965 |
| sortino_ratio | -11.0795 |
| max_drawdown | 1.0000 |
| cagr | -0.9970 |
| net_avg_win | 4.2993 |
| net_avg_loss | -10.7560 |
| avg_hold_time_bars | 2.3502 |
| exposure | 0.1608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
