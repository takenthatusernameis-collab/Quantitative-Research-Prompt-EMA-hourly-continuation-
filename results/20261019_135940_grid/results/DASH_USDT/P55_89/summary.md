# EMA Hourly Continuation — DASH/USDT P55_89

**Symbol:** DASH/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.3447 |
| net_win_rate | 0.4405 |
| gross_profit_factor | 0.8234 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -7.1456 |
| sortino_ratio | -2.6586 |
| max_drawdown | 0.9676 |
| cagr | -0.7390 |
| net_avg_win | 16.5495 |
| net_avg_loss | -37.7894 |
| avg_hold_time_bars | 3.6055 |
| exposure | 0.1142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
