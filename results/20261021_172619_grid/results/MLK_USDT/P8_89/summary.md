# EMA Hourly Continuation — MLK/USDT P8_89

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.5779 |
| net_win_rate | 0.4173 |
| gross_profit_factor | 0.7743 |
| gross_win_rate | 0.4208 |
| sharpe_ratio | -4.5057 |
| sortino_ratio | -1.5159 |
| max_drawdown | 0.8379 |
| cagr | -0.5050 |
| net_avg_win | 47.9610 |
| net_avg_loss | -59.4260 |
| avg_hold_time_bars | 19.5651 |
| exposure | 0.5029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
