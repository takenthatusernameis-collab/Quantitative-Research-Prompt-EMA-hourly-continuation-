# EMA Hourly Continuation — PENDLE/USDT P12_100

**Symbol:** PENDLE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.6351 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.8812 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -3.4017 |
| sortino_ratio | -1.1992 |
| max_drawdown | 0.7685 |
| cagr | -0.4319 |
| net_avg_win | 44.7438 |
| net_avg_loss | -62.5962 |
| avg_hold_time_bars | 20.8214 |
| exposure | 0.5934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
