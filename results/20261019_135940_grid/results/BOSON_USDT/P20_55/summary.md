# EMA Hourly Continuation — BOSON/USDT P20_55

**Symbol:** BOSON/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 886 |
| net_profit_factor | 0.5809 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.8904 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -5.4918 |
| sortino_ratio | -2.2901 |
| max_drawdown | 0.9379 |
| cagr | -0.6681 |
| net_avg_win | 32.4044 |
| net_avg_loss | -46.1187 |
| avg_hold_time_bars | 6.5892 |
| exposure | 0.2654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
