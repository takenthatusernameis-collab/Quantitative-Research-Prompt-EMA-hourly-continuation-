# EMA Hourly Continuation — AZERO/USDT P8_50

**Symbol:** AZERO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1043 |
| net_profit_factor | 0.6477 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 1.0317 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -4.8824 |
| sortino_ratio | -2.2047 |
| max_drawdown | 0.9414 |
| cagr | -0.6560 |
| net_avg_win | 34.2716 |
| net_avg_loss | -48.7258 |
| avg_hold_time_bars | 9.2924 |
| exposure | 0.4386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
