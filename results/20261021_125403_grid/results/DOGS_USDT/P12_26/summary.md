# EMA Hourly Continuation — DOGS/USDT P12_26

**Symbol:** DOGS/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.6756 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.8709 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -2.1292 |
| sortino_ratio | -0.5666 |
| max_drawdown | 0.4720 |
| cagr | -0.2283 |
| net_avg_win | 63.1426 |
| net_avg_loss | -83.9329 |
| avg_hold_time_bars | 5.6174 |
| exposure | 0.0888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
