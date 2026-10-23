# EMA Hourly Continuation — YGG/USDT P8_200

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.7936 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0633 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -1.5966 |
| sortino_ratio | -0.4608 |
| max_drawdown | 0.5029 |
| cagr | -0.1964 |
| net_avg_win | 77.6157 |
| net_avg_loss | -99.2214 |
| avg_hold_time_bars | 41.3022 |
| exposure | 0.7794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
