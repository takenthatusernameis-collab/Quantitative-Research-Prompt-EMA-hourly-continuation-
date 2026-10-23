# EMA Hourly Continuation — EUL/USDT P21_89

**Symbol:** EUL/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.4827 |
| net_win_rate | 0.4335 |
| gross_profit_factor | 0.7028 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -4.9962 |
| sortino_ratio | -1.8047 |
| max_drawdown | 0.8921 |
| cagr | -0.5827 |
| net_avg_win | 28.5884 |
| net_avg_loss | -45.3204 |
| avg_hold_time_bars | 11.7788 |
| exposure | 0.3582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
