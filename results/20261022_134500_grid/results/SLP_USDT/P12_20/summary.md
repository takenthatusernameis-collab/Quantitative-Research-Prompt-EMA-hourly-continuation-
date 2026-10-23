# EMA Hourly Continuation — SLP/USDT P12_20

**Symbol:** SLP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1623 |
| net_profit_factor | 0.2663 |
| net_win_rate | 0.3802 |
| gross_profit_factor | 0.7107 |
| gross_win_rate | 0.4104 |
| sharpe_ratio | -15.0261 |
| sortino_ratio | -8.6856 |
| max_drawdown | 1.0000 |
| cagr | -0.9885 |
| net_avg_win | 5.8818 |
| net_avg_loss | -13.5477 |
| avg_hold_time_bars | 2.4036 |
| exposure | 0.1773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
