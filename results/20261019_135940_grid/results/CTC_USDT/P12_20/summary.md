# EMA Hourly Continuation — CTC/USDT P12_20

**Symbol:** CTC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1479 |
| net_profit_factor | 0.2281 |
| net_win_rate | 0.3942 |
| gross_profit_factor | 0.7392 |
| gross_win_rate | 0.4544 |
| sharpe_ratio | -13.9061 |
| sortino_ratio | -7.6259 |
| max_drawdown | 1.0000 |
| cagr | -0.9816 |
| net_avg_win | 5.0683 |
| net_avg_loss | -14.4580 |
| avg_hold_time_bars | 2.8188 |
| exposure | 0.1895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
