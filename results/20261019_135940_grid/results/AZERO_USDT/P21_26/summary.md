# EMA Hourly Continuation — AZERO/USDT P21_26

**Symbol:** AZERO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1041 |
| net_profit_factor | 0.2242 |
| net_win_rate | 0.3497 |
| gross_profit_factor | 0.7485 |
| gross_win_rate | 0.3852 |
| sharpe_ratio | -13.2060 |
| sortino_ratio | -6.1230 |
| max_drawdown | 0.9998 |
| cagr | -0.9628 |
| net_avg_win | 7.9396 |
| net_avg_loss | -19.0362 |
| avg_hold_time_bars | 2.6676 |
| exposure | 0.1257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
