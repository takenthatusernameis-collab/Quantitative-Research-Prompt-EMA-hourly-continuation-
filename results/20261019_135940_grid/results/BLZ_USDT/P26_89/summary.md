# EMA Hourly Continuation — BLZ/USDT P26_89

**Symbol:** BLZ/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 748 |
| net_profit_factor | 0.5492 |
| net_win_rate | 0.4118 |
| gross_profit_factor | 0.8333 |
| gross_win_rate | 0.4238 |
| sharpe_ratio | -6.4363 |
| sortino_ratio | -2.4816 |
| max_drawdown | 0.9516 |
| cagr | -0.6924 |
| net_avg_win | 37.5321 |
| net_avg_loss | -47.8378 |
| avg_hold_time_bars | 10.1765 |
| exposure | 0.3445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
