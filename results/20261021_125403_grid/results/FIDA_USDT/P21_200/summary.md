# EMA Hourly Continuation — FIDA/USDT P21_200

**Symbol:** FIDA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.6903 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.8440 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -1.9880 |
| sortino_ratio | -0.4954 |
| max_drawdown | 0.4592 |
| cagr | -0.2046 |
| net_avg_win | 68.3698 |
| net_avg_loss | -84.8142 |
| avg_hold_time_bars | 45.1129 |
| exposure | 0.6328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
