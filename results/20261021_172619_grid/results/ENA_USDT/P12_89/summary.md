# EMA Hourly Continuation — ENA/USDT P12_89

**Symbol:** ENA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.9707 |
| net_win_rate | 0.5301 |
| gross_profit_factor | 1.1187 |
| gross_win_rate | 0.5301 |
| sharpe_ratio | -0.1386 |
| sortino_ratio | -0.0447 |
| max_drawdown | 0.2943 |
| cagr | -0.0289 |
| net_avg_win | 89.1515 |
| net_avg_loss | -103.6145 |
| avg_hold_time_bars | 22.2329 |
| exposure | 0.5033 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
