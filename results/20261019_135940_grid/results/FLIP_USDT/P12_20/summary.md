# EMA Hourly Continuation — FLIP/USDT P12_20

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1061 |
| net_profit_factor | 0.2750 |
| net_win_rate | 0.3167 |
| gross_profit_factor | 0.8294 |
| gross_win_rate | 0.3959 |
| sharpe_ratio | -14.4882 |
| sortino_ratio | -6.9110 |
| max_drawdown | 0.9999 |
| cagr | -0.9758 |
| net_avg_win | 11.2865 |
| net_avg_loss | -19.0226 |
| avg_hold_time_bars | 4.7512 |
| exposure | 0.2291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
