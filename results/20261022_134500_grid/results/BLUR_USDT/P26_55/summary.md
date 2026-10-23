# EMA Hourly Continuation — BLUR/USDT P26_55

**Symbol:** BLUR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 903 |
| net_profit_factor | 0.5402 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.9403 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -5.9887 |
| sortino_ratio | -2.5266 |
| max_drawdown | 0.9561 |
| cagr | -0.7063 |
| net_avg_win | 26.5756 |
| net_avg_loss | -43.1605 |
| avg_hold_time_bars | 4.6202 |
| exposure | 0.1888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
