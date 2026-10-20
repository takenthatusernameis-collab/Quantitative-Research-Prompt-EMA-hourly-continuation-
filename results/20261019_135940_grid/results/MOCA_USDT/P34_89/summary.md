# EMA Hourly Continuation — MOCA/USDT P34_89

**Symbol:** MOCA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5361 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.8534 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -5.6439 |
| sortino_ratio | -2.0863 |
| max_drawdown | 0.9157 |
| cagr | -0.6464 |
| net_avg_win | 36.6139 |
| net_avg_loss | -55.8122 |
| avg_hold_time_bars | 7.6887 |
| exposure | 0.2451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
