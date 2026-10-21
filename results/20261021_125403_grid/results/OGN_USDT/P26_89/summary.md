# EMA Hourly Continuation — OGN/USDT P26_89

**Symbol:** OGN/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.6913 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.9224 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -3.1553 |
| sortino_ratio | -1.0309 |
| max_drawdown | 0.7229 |
| cagr | -0.3776 |
| net_avg_win | 63.2455 |
| net_avg_loss | -80.1331 |
| avg_hold_time_bars | 12.8072 |
| exposure | 0.3066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
