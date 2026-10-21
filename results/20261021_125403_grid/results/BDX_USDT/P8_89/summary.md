# EMA Hourly Continuation — BDX/USDT P8_89

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.5189 |
| net_win_rate | 0.4085 |
| gross_profit_factor | 0.7719 |
| gross_win_rate | 0.4085 |
| sharpe_ratio | -5.8946 |
| sortino_ratio | -2.0322 |
| max_drawdown | 0.9130 |
| cagr | -0.6145 |
| net_avg_win | 41.0092 |
| net_avg_loss | -54.5906 |
| avg_hold_time_bars | 12.5350 |
| exposure | 0.3333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
