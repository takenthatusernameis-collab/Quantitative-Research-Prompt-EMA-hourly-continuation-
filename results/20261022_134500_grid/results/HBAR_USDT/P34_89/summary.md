# EMA Hourly Continuation — HBAR/USDT P34_89

**Symbol:** HBAR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 699 |
| net_profit_factor | 0.5740 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 1.0425 |
| gross_win_rate | 0.4993 |
| sharpe_ratio | -4.9231 |
| sortino_ratio | -1.8290 |
| max_drawdown | 0.8943 |
| cagr | -0.5907 |
| net_avg_win | 35.6352 |
| net_avg_loss | -58.1265 |
| avg_hold_time_bars | 6.7811 |
| exposure | 0.2155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
