# EMA Hourly Continuation — APE/USDT P26_50

**Symbol:** APE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 974 |
| net_profit_factor | 0.4641 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.9015 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -7.4107 |
| sortino_ratio | -3.2635 |
| max_drawdown | 0.9830 |
| cagr | -0.7984 |
| net_avg_win | 18.8977 |
| net_avg_loss | -34.9711 |
| avg_hold_time_bars | 3.2988 |
| exposure | 0.1460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
