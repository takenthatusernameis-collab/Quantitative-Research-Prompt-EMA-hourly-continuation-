# EMA Hourly Continuation — LUNA/USDT P8_55

**Symbol:** LUNA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.7182 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.9109 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -3.3060 |
| sortino_ratio | -1.2165 |
| max_drawdown | 0.7594 |
| cagr | -0.4293 |
| net_avg_win | 62.5095 |
| net_avg_loss | -74.2592 |
| avg_hold_time_bars | 13.3662 |
| exposure | 0.4065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
