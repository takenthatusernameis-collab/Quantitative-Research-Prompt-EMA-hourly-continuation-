# EMA Hourly Continuation — AGLD/USDT P26_34

**Symbol:** AGLD/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1057 |
| net_profit_factor | 0.3670 |
| net_win_rate | 0.3992 |
| gross_profit_factor | 0.8577 |
| gross_win_rate | 0.4494 |
| sharpe_ratio | -10.2692 |
| sortino_ratio | -4.7541 |
| max_drawdown | 0.9974 |
| cagr | -0.9063 |
| net_avg_win | 13.7049 |
| net_avg_loss | -24.8157 |
| avg_hold_time_bars | 3.0104 |
| exposure | 0.1440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
