# EMA Hourly Continuation — MOVR/USDT P26_89

**Symbol:** MOVR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.6921 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.8750 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -2.7685 |
| sortino_ratio | -0.8889 |
| max_drawdown | 0.6840 |
| cagr | -0.3363 |
| net_avg_win | 61.4865 |
| net_avg_loss | -75.9169 |
| avg_hold_time_bars | 12.0196 |
| exposure | 0.2786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
