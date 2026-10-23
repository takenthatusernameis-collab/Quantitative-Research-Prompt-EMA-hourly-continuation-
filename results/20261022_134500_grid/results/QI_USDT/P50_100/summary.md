# EMA Hourly Continuation — QI/USDT P50_100

**Symbol:** QI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.4830 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.8909 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -4.8635 |
| sortino_ratio | -1.6567 |
| max_drawdown | 0.8720 |
| cagr | -0.5502 |
| net_avg_win | 29.8730 |
| net_avg_loss | -53.3841 |
| avg_hold_time_bars | 6.7556 |
| exposure | 0.1788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
