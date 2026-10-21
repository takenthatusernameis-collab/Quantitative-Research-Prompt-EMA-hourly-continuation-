# EMA Hourly Continuation — BAND/USDT P8_89

**Symbol:** BAND/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.7472 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9344 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -2.4674 |
| sortino_ratio | -0.8163 |
| max_drawdown | 0.6415 |
| cagr | -0.3156 |
| net_avg_win | 70.5565 |
| net_avg_loss | -84.8844 |
| avg_hold_time_bars | 25.0936 |
| exposure | 0.6189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
