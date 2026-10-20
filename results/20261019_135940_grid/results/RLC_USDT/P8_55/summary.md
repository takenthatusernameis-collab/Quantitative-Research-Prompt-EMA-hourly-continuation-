# EMA Hourly Continuation — RLC/USDT P8_55

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1019 |
| net_profit_factor | 0.6236 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.9855 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -5.4658 |
| sortino_ratio | -2.4493 |
| max_drawdown | 0.9526 |
| cagr | -0.6939 |
| net_avg_win | 32.6788 |
| net_avg_loss | -46.8532 |
| avg_hold_time_bars | 10.6644 |
| exposure | 0.4940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
