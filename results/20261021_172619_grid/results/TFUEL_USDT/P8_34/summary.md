# EMA Hourly Continuation — TFUEL/USDT P8_34

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 820 |
| net_profit_factor | 0.6472 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8957 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -4.9352 |
| sortino_ratio | -2.0096 |
| max_drawdown | 0.9039 |
| cagr | -0.6031 |
| net_avg_win | 45.0085 |
| net_avg_loss | -56.6174 |
| avg_hold_time_bars | 7.4902 |
| exposure | 0.2779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
