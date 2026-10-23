# EMA Hourly Continuation — MINA/USDT P12_50

**Symbol:** MINA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 988 |
| net_profit_factor | 0.6071 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 1.0103 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -5.4718 |
| sortino_ratio | -2.4086 |
| max_drawdown | 0.9530 |
| cagr | -0.6912 |
| net_avg_win | 31.0194 |
| net_avg_loss | -46.7407 |
| avg_hold_time_bars | 8.8785 |
| exposure | 0.3987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
