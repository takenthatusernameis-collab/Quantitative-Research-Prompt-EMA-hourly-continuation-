# EMA Hourly Continuation — CELR/USDT P12_100

**Symbol:** CELR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.6328 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.9046 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -3.8118 |
| sortino_ratio | -1.3259 |
| max_drawdown | 0.8015 |
| cagr | -0.4641 |
| net_avg_win | 48.2683 |
| net_avg_loss | -65.8148 |
| avg_hold_time_bars | 21.4861 |
| exposure | 0.5941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
