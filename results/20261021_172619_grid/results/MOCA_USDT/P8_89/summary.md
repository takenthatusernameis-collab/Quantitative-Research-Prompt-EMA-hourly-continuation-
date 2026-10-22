# EMA Hourly Continuation — MOCA/USDT P8_89

**Symbol:** MOCA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.8649 |
| net_win_rate | 0.5187 |
| gross_profit_factor | 1.0718 |
| gross_win_rate | 0.5187 |
| sharpe_ratio | -1.0068 |
| sortino_ratio | -0.3141 |
| max_drawdown | 0.4008 |
| cagr | -0.1373 |
| net_avg_win | 82.3832 |
| net_avg_loss | -102.6466 |
| avg_hold_time_bars | 30.4883 |
| exposure | 0.6542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
