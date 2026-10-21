# EMA Hourly Continuation — BDX/USDT P20_26

**Symbol:** BDX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 148 |
| net_profit_factor | 0.3561 |
| net_win_rate | 0.3514 |
| gross_profit_factor | 0.5942 |
| gross_win_rate | 0.3514 |
| sharpe_ratio | -3.9712 |
| sortino_ratio | -0.6952 |
| max_drawdown | 0.5741 |
| cagr | -0.2767 |
| net_avg_win | 59.2106 |
| net_avg_loss | -90.0662 |
| avg_hold_time_bars | 3.7635 |
| exposure | 0.0253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
