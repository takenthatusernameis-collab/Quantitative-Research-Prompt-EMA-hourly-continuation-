# EMA Hourly Continuation — JASMY/USDT P34_50

**Symbol:** JASMY/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 927 |
| net_profit_factor | 0.4124 |
| net_win_rate | 0.4164 |
| gross_profit_factor | 0.7956 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -9.4340 |
| sortino_ratio | -4.0976 |
| max_drawdown | 0.9944 |
| cagr | -0.8717 |
| net_avg_win | 18.0776 |
| net_avg_loss | -31.2760 |
| avg_hold_time_bars | 2.2999 |
| exposure | 0.0969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
