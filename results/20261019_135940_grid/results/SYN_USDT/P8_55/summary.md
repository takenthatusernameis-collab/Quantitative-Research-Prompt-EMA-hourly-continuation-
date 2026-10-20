# EMA Hourly Continuation — SYN/USDT P8_55

**Symbol:** SYN/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 991 |
| net_profit_factor | 0.6281 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.9565 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -5.0638 |
| sortino_ratio | -2.2203 |
| max_drawdown | 0.9364 |
| cagr | -0.6627 |
| net_avg_win | 33.9493 |
| net_avg_loss | -47.7825 |
| avg_hold_time_bars | 11.0737 |
| exposure | 0.4988 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
