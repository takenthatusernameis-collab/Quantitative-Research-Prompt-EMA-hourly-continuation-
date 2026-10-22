# EMA Hourly Continuation — KCS/USDT P12_200

**Symbol:** KCS/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.4355 |
| net_win_rate | 0.4213 |
| gross_profit_factor | 0.9331 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -5.7453 |
| sortino_ratio | -1.6654 |
| max_drawdown | 0.8866 |
| cagr | -0.5770 |
| net_avg_win | 37.5065 |
| net_avg_loss | -62.6955 |
| avg_hold_time_bars | 35.3634 |
| exposure | 0.6944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
