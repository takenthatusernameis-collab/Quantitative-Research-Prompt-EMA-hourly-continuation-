# EMA Hourly Continuation — PUNDIX/USDT P26_50

**Symbol:** PUNDIX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.6670 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 1.0244 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -3.1754 |
| sortino_ratio | -1.0365 |
| max_drawdown | 0.7103 |
| cagr | -0.3770 |
| net_avg_win | 54.4008 |
| net_avg_loss | -80.3065 |
| avg_hold_time_bars | 6.7616 |
| exposure | 0.1586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
