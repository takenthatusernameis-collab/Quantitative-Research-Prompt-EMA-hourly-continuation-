# EMA Hourly Continuation — BSV/USDT P26_89

**Symbol:** BSV/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.6551 |
| net_win_rate | 0.4721 |
| gross_profit_factor | 0.8908 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -2.9805 |
| sortino_ratio | -0.9524 |
| max_drawdown | 0.6713 |
| cagr | -0.3525 |
| net_avg_win | 53.2455 |
| net_avg_loss | -72.6857 |
| avg_hold_time_bars | 13.6116 |
| exposure | 0.3106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
