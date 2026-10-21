# EMA Hourly Continuation — GRAM/USDT P12_50

**Symbol:** GRAM/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.7255 |
| net_win_rate | 0.5009 |
| gross_profit_factor | 1.0072 |
| gross_win_rate | 0.5009 |
| sharpe_ratio | -2.4641 |
| sortino_ratio | -0.8553 |
| max_drawdown | 0.6520 |
| cagr | -0.3240 |
| net_avg_win | 56.4677 |
| net_avg_loss | -78.0973 |
| avg_hold_time_bars | 10.7231 |
| exposure | 0.2851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
