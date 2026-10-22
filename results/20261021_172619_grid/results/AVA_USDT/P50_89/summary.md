# EMA Hourly Continuation — AVA/USDT P50_89

**Symbol:** AVA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.8132 |
| net_win_rate | 0.5288 |
| gross_profit_factor | 1.1247 |
| gross_win_rate | 0.5288 |
| sharpe_ratio | -1.2669 |
| sortino_ratio | -0.3497 |
| max_drawdown | 0.3940 |
| cagr | -0.1486 |
| net_avg_win | 74.9852 |
| net_avg_loss | -103.4680 |
| avg_hold_time_bars | 6.1370 |
| exposure | 0.1018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
