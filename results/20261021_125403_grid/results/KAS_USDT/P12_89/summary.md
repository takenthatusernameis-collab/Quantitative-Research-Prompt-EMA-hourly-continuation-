# EMA Hourly Continuation — KAS/USDT P12_89

**Symbol:** KAS/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.8343 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.0310 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -1.1585 |
| sortino_ratio | -0.3748 |
| max_drawdown | 0.3757 |
| cagr | -0.1606 |
| net_avg_win | 68.6381 |
| net_avg_loss | -86.9330 |
| avg_hold_time_bars | 21.5768 |
| exposure | 0.4982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
