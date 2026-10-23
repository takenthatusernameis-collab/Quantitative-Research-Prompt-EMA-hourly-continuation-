# EMA Hourly Continuation — MOVR/USDT P12_50

**Symbol:** MOVR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1103 |
| net_profit_factor | 0.4862 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8526 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -7.0039 |
| sortino_ratio | -3.2336 |
| max_drawdown | 0.9827 |
| cagr | -0.8009 |
| net_avg_win | 18.6690 |
| net_avg_loss | -31.6090 |
| avg_hold_time_bars | 7.3744 |
| exposure | 0.3697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
