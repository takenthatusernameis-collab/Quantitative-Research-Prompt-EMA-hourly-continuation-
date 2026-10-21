# EMA Hourly Continuation — KMNO/USDT P20_55

**Symbol:** KMNO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.7118 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9424 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -2.3673 |
| sortino_ratio | -0.7545 |
| max_drawdown | 0.5924 |
| cagr | -0.2942 |
| net_avg_win | 59.6670 |
| net_avg_loss | -79.5057 |
| avg_hold_time_bars | 8.9409 |
| exposure | 0.2027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
