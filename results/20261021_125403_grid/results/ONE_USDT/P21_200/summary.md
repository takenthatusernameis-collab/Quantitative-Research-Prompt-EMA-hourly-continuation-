# EMA Hourly Continuation — ONE/USDT P21_200

**Symbol:** ONE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.8630 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 1.0049 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -0.7902 |
| sortino_ratio | -0.1873 |
| max_drawdown | 0.2805 |
| cagr | -0.0846 |
| net_avg_win | 90.9460 |
| net_avg_loss | -106.1477 |
| avg_hold_time_bars | 53.3091 |
| exposure | 0.6664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
