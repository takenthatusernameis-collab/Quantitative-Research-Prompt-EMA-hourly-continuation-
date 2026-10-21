# EMA Hourly Continuation — FLOKI/USDT P8_12

**Symbol:** FLOKI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.8267 |
| net_win_rate | 0.5270 |
| gross_profit_factor | 1.1290 |
| gross_win_rate | 0.5270 |
| sharpe_ratio | -0.9657 |
| sortino_ratio | -0.2077 |
| max_drawdown | 0.2920 |
| cagr | -0.0915 |
| net_avg_win | 87.3628 |
| net_avg_loss | -117.7468 |
| avg_hold_time_bars | 3.9910 |
| exposure | 0.0403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
