# EMA Hourly Continuation — LUNC/USDT P8_89

**Symbol:** LUNC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.6491 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8205 |
| gross_win_rate | 0.4501 |
| sharpe_ratio | -3.2074 |
| sortino_ratio | -1.0683 |
| max_drawdown | 0.7173 |
| cagr | -0.3891 |
| net_avg_win | 52.9528 |
| net_avg_loss | -66.7690 |
| avg_hold_time_bars | 23.6915 |
| exposure | 0.5934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
