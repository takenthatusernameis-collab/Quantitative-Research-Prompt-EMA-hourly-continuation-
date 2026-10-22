# EMA Hourly Continuation — DOGS/USDT P20_55

**Symbol:** DOGS/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.7020 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.8674 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -2.2305 |
| sortino_ratio | -0.6882 |
| max_drawdown | 0.5008 |
| cagr | -0.2709 |
| net_avg_win | 61.1403 |
| net_avg_loss | -78.0616 |
| avg_hold_time_bars | 8.8010 |
| exposure | 0.1877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
