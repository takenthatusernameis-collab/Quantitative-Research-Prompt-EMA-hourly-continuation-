# EMA Hourly Continuation — BLUR/USDT P21_26

**Symbol:** BLUR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1187 |
| net_profit_factor | 0.2095 |
| net_win_rate | 0.3555 |
| gross_profit_factor | 0.6424 |
| gross_win_rate | 0.4086 |
| sharpe_ratio | -14.1376 |
| sortino_ratio | -7.0170 |
| max_drawdown | 0.9999 |
| cagr | -0.9756 |
| net_avg_win | 6.2802 |
| net_avg_loss | -16.5351 |
| avg_hold_time_bars | 2.0143 |
| exposure | 0.1082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
