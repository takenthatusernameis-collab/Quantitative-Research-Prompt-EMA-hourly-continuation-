# EMA Hourly Continuation — PENDLE/USDT P34_89

**Symbol:** PENDLE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.7749 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9615 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -1.6552 |
| sortino_ratio | -0.5080 |
| max_drawdown | 0.4552 |
| cagr | -0.2090 |
| net_avg_win | 67.4732 |
| net_avg_loss | -84.8351 |
| avg_hold_time_bars | 9.8609 |
| exposure | 0.2062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
