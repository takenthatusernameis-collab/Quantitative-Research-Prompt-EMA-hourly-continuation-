# EMA Hourly Continuation — ALEX/USDT P26_34

**Symbol:** ALEX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.3256 |
| net_win_rate | 0.3069 |
| gross_profit_factor | 0.8368 |
| gross_win_rate | 0.3450 |
| sharpe_ratio | -13.6685 |
| sortino_ratio | -6.1101 |
| max_drawdown | 0.9998 |
| cagr | -0.9653 |
| net_avg_win | 16.1998 |
| net_avg_loss | -22.0288 |
| avg_hold_time_bars | 2.7590 |
| exposure | 0.1218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
