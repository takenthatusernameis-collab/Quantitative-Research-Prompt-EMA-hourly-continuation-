# EMA Hourly Continuation — DOGE/USDT P20_21

**Symbol:** DOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1185 |
| net_profit_factor | 0.0971 |
| net_win_rate | 0.2565 |
| gross_profit_factor | 0.5511 |
| gross_win_rate | 0.3359 |
| sharpe_ratio | -19.4695 |
| sortino_ratio | -10.6059 |
| max_drawdown | 1.0000 |
| cagr | -0.9977 |
| net_avg_win | 3.5390 |
| net_avg_loss | -12.5719 |
| avg_hold_time_bars | 1.5544 |
| exposure | 0.0837 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
