# EMA Hourly Continuation — COTI/USDT P8_21

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1720 |
| net_profit_factor | 0.5359 |
| net_win_rate | 0.4355 |
| gross_profit_factor | 1.0452 |
| gross_win_rate | 0.4494 |
| sharpe_ratio | -11.2287 |
| sortino_ratio | -6.5400 |
| max_drawdown | 0.9997 |
| cagr | -0.9625 |
| net_avg_win | 15.4157 |
| net_avg_loss | -22.1872 |
| avg_hold_time_bars | 2.8657 |
| exposure | 0.2240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
