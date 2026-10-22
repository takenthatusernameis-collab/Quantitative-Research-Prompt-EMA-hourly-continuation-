# EMA Hourly Continuation — QI/USDT P12_20

**Symbol:** QI/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.6244 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9794 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -3.4309 |
| sortino_ratio | -1.1250 |
| max_drawdown | 0.7323 |
| cagr | -0.4036 |
| net_avg_win | 46.7699 |
| net_avg_loss | -73.4798 |
| avg_hold_time_bars | 5.1319 |
| exposure | 0.1215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
