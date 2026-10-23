# EMA Hourly Continuation — SATS/USDT P20_34

**Symbol:** SATS/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 954 |
| net_profit_factor | 0.4848 |
| net_win_rate | 0.4413 |
| gross_profit_factor | 0.9780 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -7.5319 |
| sortino_ratio | -3.2713 |
| max_drawdown | 0.9836 |
| cagr | -0.8006 |
| net_avg_win | 21.9725 |
| net_avg_loss | -35.7960 |
| avg_hold_time_bars | 3.2348 |
| exposure | 0.1396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
