# EMA Hourly Continuation — JST/USDT P8_50

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 901 |
| net_profit_factor | 0.3281 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.9312 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -8.2819 |
| sortino_ratio | -3.4667 |
| max_drawdown | 0.9893 |
| cagr | -0.8331 |
| net_avg_win | 12.0120 |
| net_avg_loss | -29.4981 |
| avg_hold_time_bars | 11.2819 |
| exposure | 0.4600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
