# EMA Hourly Continuation — BDX/USDT P21_34

**Symbol:** BDX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 176 |
| net_profit_factor | 0.3435 |
| net_win_rate | 0.3466 |
| gross_profit_factor | 0.5713 |
| gross_win_rate | 0.3466 |
| sharpe_ratio | -4.4634 |
| sortino_ratio | -0.8530 |
| max_drawdown | 0.6477 |
| cagr | -0.3325 |
| net_avg_win | 54.6995 |
| net_avg_loss | -84.4576 |
| avg_hold_time_bars | 4.4091 |
| exposure | 0.0353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
