# EMA Hourly Continuation — IOST/USDT P34_89

**Symbol:** IOST/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.8009 |
| net_win_rate | 0.5289 |
| gross_profit_factor | 1.1102 |
| gross_win_rate | 0.5289 |
| sharpe_ratio | -1.4152 |
| sortino_ratio | -0.4330 |
| max_drawdown | 0.4429 |
| cagr | -0.1811 |
| net_avg_win | 66.6872 |
| net_avg_loss | -93.4726 |
| avg_hold_time_bars | 11.6667 |
| exposure | 0.2386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
