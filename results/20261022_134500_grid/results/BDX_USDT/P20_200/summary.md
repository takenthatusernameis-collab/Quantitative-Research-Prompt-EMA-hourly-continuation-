# EMA Hourly Continuation — BDX/USDT P20_200

**Symbol:** BDX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 950 |
| net_profit_factor | 0.3727 |
| net_win_rate | 0.3368 |
| gross_profit_factor | 0.7533 |
| gross_win_rate | 0.3747 |
| sharpe_ratio | -12.7386 |
| sortino_ratio | -5.6475 |
| max_drawdown | 0.9996 |
| cagr | -0.9522 |
| net_avg_win | 18.5538 |
| net_avg_loss | -25.2895 |
| avg_hold_time_bars | 10.3853 |
| exposure | 0.4485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
