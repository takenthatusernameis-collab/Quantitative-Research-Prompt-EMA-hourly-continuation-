# EMA Hourly Continuation — NYM/USDT P12_20

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.3045 |
| net_win_rate | 0.4040 |
| gross_profit_factor | 0.6607 |
| gross_win_rate | 0.4153 |
| sharpe_ratio | -5.6157 |
| sortino_ratio | -1.5173 |
| max_drawdown | 0.8403 |
| cagr | -0.5134 |
| net_avg_win | 25.6010 |
| net_avg_loss | -56.9807 |
| avg_hold_time_bars | 9.4802 |
| exposure | 0.1525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
