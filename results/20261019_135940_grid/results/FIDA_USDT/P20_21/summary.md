# EMA Hourly Continuation — FIDA/USDT P20_21

**Symbol:** FIDA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1202 |
| net_profit_factor | 0.1975 |
| net_win_rate | 0.3261 |
| gross_profit_factor | 0.7698 |
| gross_win_rate | 0.4110 |
| sharpe_ratio | -15.8236 |
| sortino_ratio | -8.1029 |
| max_drawdown | 1.0000 |
| cagr | -0.9874 |
| net_avg_win | 6.2786 |
| net_avg_loss | -15.3840 |
| avg_hold_time_bars | 2.3020 |
| exposure | 0.1252 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
