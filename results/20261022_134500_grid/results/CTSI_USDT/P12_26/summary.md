# EMA Hourly Continuation — CTSI/USDT P12_26

**Symbol:** CTSI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1317 |
| net_profit_factor | 0.4377 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.9792 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -9.4731 |
| sortino_ratio | -4.8849 |
| max_drawdown | 0.9975 |
| cagr | -0.9072 |
| net_avg_win | 13.2492 |
| net_avg_loss | -24.2661 |
| avg_hold_time_bars | 3.7236 |
| exposure | 0.2229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
