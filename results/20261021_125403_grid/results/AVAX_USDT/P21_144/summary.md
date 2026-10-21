# EMA Hourly Continuation — AVAX/USDT P21_144

**Symbol:** AVAX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7900 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9690 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -1.5979 |
| sortino_ratio | -0.4365 |
| max_drawdown | 0.4772 |
| cagr | -0.1827 |
| net_avg_win | 83.9954 |
| net_avg_loss | -100.6701 |
| avg_hold_time_bars | 27.7978 |
| exposure | 0.4625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
