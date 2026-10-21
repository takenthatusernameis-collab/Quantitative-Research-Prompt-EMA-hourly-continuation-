# EMA Hourly Continuation — CKB/USDT P50_55

**Symbol:** CKB/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 140 |
| net_profit_factor | 0.5805 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8731 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -2.0439 |
| sortino_ratio | -0.3460 |
| max_drawdown | 0.3356 |
| cagr | -0.1477 |
| net_avg_win | 70.3934 |
| net_avg_loss | -105.0969 |
| avg_hold_time_bars | 4.9571 |
| exposure | 0.0315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
