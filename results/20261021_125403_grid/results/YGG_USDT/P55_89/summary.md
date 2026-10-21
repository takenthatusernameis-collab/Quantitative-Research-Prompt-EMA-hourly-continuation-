# EMA Hourly Continuation — YGG/USDT P55_89

**Symbol:** YGG/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7972 |
| net_win_rate | 0.5213 |
| gross_profit_factor | 1.0763 |
| gross_win_rate | 0.5213 |
| sharpe_ratio | -1.3312 |
| sortino_ratio | -0.3712 |
| max_drawdown | 0.3727 |
| cagr | -0.1571 |
| net_avg_win | 70.2700 |
| net_avg_loss | -95.9773 |
| avg_hold_time_bars | 6.1995 |
| exposure | 0.1055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
