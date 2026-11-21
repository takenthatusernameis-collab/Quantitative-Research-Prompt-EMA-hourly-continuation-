# EMA Hourly Continuation — HTR/USDT P20_200

**Symbol:** HTR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.5785 |
| net_win_rate | 0.4172 |
| gross_profit_factor | 0.8127 |
| gross_win_rate | 0.4301 |
| sharpe_ratio | -4.6693 |
| sortino_ratio | -1.3924 |
| max_drawdown | 0.8322 |
| cagr | -0.5046 |
| net_avg_win | 58.6139 |
| net_avg_loss | -72.5376 |
| avg_hold_time_bars | 28.9355 |
| exposure | 0.6116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
