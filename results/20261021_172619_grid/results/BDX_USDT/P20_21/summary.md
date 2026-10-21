# EMA Hourly Continuation — BDX/USDT P20_21

**Symbol:** BDX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 125 |
| net_profit_factor | 0.2780 |
| net_win_rate | 0.3120 |
| gross_profit_factor | 0.4741 |
| gross_win_rate | 0.3120 |
| sharpe_ratio | -4.1660 |
| sortino_ratio | -0.6716 |
| max_drawdown | 0.5449 |
| cagr | -0.2691 |
| net_avg_win | 53.7910 |
| net_avg_loss | -87.7597 |
| avg_hold_time_bars | 3.4320 |
| exposure | 0.0195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
