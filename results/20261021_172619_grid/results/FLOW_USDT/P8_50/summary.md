# EMA Hourly Continuation — FLOW/USDT P8_50

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.7022 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9167 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -2.8403 |
| sortino_ratio | -1.0861 |
| max_drawdown | 0.7291 |
| cagr | -0.3927 |
| net_avg_win | 48.8227 |
| net_avg_loss | -64.3063 |
| avg_hold_time_bars | 13.4304 |
| exposure | 0.4383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
