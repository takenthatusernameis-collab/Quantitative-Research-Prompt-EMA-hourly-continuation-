# EMA Hourly Continuation — POPCAT/USDT P50_55

**Symbol:** POPCAT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 775 |
| net_profit_factor | 0.3432 |
| net_win_rate | 0.3677 |
| gross_profit_factor | 0.6737 |
| gross_win_rate | 0.3987 |
| sharpe_ratio | -11.2699 |
| sortino_ratio | -4.8164 |
| max_drawdown | 0.9960 |
| cagr | -0.9228 |
| net_avg_win | 18.2601 |
| net_avg_loss | -30.9481 |
| avg_hold_time_bars | 1.9961 |
| exposure | 0.0817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
