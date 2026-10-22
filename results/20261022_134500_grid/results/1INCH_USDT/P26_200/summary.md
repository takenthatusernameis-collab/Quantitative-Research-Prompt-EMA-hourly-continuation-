# EMA Hourly Continuation — 1INCH/USDT P26_200

**Symbol:** 1INCH/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.6666 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9576 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -2.3961 |
| sortino_ratio | -0.6325 |
| max_drawdown | 0.5452 |
| cagr | -0.2587 |
| net_avg_win | 61.7835 |
| net_avg_loss | -88.5454 |
| avg_hold_time_bars | 39.8743 |
| exposure | 0.6344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
