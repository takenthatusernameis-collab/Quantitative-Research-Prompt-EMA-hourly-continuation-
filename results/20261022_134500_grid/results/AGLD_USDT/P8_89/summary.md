# EMA Hourly Continuation — AGLD/USDT P8_89

**Symbol:** AGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.7496 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 1.0525 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -2.5886 |
| sortino_ratio | -0.9488 |
| max_drawdown | 0.7105 |
| cagr | -0.3604 |
| net_avg_win | 60.2280 |
| net_avg_loss | -79.4031 |
| avg_hold_time_bars | 20.8905 |
| exposure | 0.6391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
