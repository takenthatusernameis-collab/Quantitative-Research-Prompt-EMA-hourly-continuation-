# EMA Hourly Continuation — POKT/USDT P12_21

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1451 |
| net_profit_factor | 0.3328 |
| net_win_rate | 0.3253 |
| gross_profit_factor | 0.8290 |
| gross_win_rate | 0.3522 |
| sharpe_ratio | -15.2580 |
| sortino_ratio | -8.2402 |
| max_drawdown | 1.0000 |
| cagr | -0.9853 |
| net_avg_win | 10.5684 |
| net_avg_loss | -15.3095 |
| avg_hold_time_bars | 3.0186 |
| exposure | 0.1982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
