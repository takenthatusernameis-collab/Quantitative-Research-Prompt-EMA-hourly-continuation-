# EMA Hourly Continuation — POKT/USDT P8_20

**Symbol:** POKT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1666 |
| net_profit_factor | 0.3802 |
| net_win_rate | 0.3553 |
| gross_profit_factor | 0.8119 |
| gross_win_rate | 0.3752 |
| sharpe_ratio | -14.4514 |
| sortino_ratio | -8.3128 |
| max_drawdown | 1.0000 |
| cagr | -0.9847 |
| net_avg_win | 10.3610 |
| net_avg_loss | -15.0219 |
| avg_hold_time_bars | 3.2671 |
| exposure | 0.2463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
