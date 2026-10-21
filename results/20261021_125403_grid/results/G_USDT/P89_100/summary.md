# EMA Hourly Continuation — G/USDT P89_100

**Symbol:** G/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.4085 |
| net_win_rate | 0.3952 |
| gross_profit_factor | 0.6472 |
| gross_win_rate | 0.3952 |
| sharpe_ratio | -3.7161 |
| sortino_ratio | -0.7412 |
| max_drawdown | 0.5297 |
| cagr | -0.2906 |
| net_avg_win | 54.9687 |
| net_avg_loss | -87.9411 |
| avg_hold_time_bars | 7.2395 |
| exposure | 0.0636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
