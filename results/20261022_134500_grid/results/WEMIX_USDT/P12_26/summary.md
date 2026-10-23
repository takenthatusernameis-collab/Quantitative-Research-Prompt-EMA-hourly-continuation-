# EMA Hourly Continuation — WEMIX/USDT P12_26

**Symbol:** WEMIX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1953 |
| net_profit_factor | 0.1757 |
| net_win_rate | 0.2796 |
| gross_profit_factor | 0.4680 |
| gross_win_rate | 0.3036 |
| sharpe_ratio | -21.9024 |
| sortino_ratio | -14.1121 |
| max_drawdown | 1.0000 |
| cagr | -0.9995 |
| net_avg_win | 3.9038 |
| net_avg_loss | -8.6222 |
| avg_hold_time_bars | 2.7542 |
| exposure | 0.2445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
