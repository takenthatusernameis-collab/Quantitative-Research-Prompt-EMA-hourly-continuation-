# EMA Hourly Continuation — CRO/USDT P20_89

**Symbol:** CRO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 748 |
| net_profit_factor | 0.4715 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.9037 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -6.8038 |
| sortino_ratio | -2.5993 |
| max_drawdown | 0.9661 |
| cagr | -0.7316 |
| net_avg_win | 26.0378 |
| net_avg_loss | -43.5999 |
| avg_hold_time_bars | 11.8275 |
| exposure | 0.4021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
