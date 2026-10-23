# EMA Hourly Continuation — CHR/USDT P12_34

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1276 |
| net_profit_factor | 0.4824 |
| net_win_rate | 0.4279 |
| gross_profit_factor | 0.8842 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -8.5879 |
| sortino_ratio | -4.3128 |
| max_drawdown | 0.9949 |
| cagr | -0.8766 |
| net_avg_win | 16.9796 |
| net_avg_loss | -26.3285 |
| avg_hold_time_bars | 4.3652 |
| exposure | 0.2520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
