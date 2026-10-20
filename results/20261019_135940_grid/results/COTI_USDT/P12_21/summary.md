# EMA Hourly Continuation — COTI/USDT P12_21

**Symbol:** COTI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1517 |
| net_profit_factor | 0.4318 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.9482 |
| gross_win_rate | 0.4423 |
| sharpe_ratio | -12.0480 |
| sortino_ratio | -6.6238 |
| max_drawdown | 0.9998 |
| cagr | -0.9664 |
| net_avg_win | 11.8894 |
| net_avg_loss | -20.0402 |
| avg_hold_time_bars | 2.2083 |
| exposure | 0.1523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
