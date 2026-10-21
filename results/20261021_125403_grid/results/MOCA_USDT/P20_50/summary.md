# EMA Hourly Continuation — MOCA/USDT P20_50

**Symbol:** MOCA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.6810 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9275 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -3.0069 |
| sortino_ratio | -1.0090 |
| max_drawdown | 0.6853 |
| cagr | -0.3693 |
| net_avg_win | 57.8059 |
| net_avg_loss | -78.3548 |
| avg_hold_time_bars | 6.5580 |
| exposure | 0.1644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
