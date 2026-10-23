# EMA Hourly Continuation — BIGTIME/USDT P12_89

**Symbol:** BIGTIME/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.7390 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0595 |
| gross_win_rate | 0.5170 |
| sharpe_ratio | -2.3173 |
| sortino_ratio | -0.8321 |
| max_drawdown | 0.6447 |
| cagr | -0.3260 |
| net_avg_win | 53.7493 |
| net_avg_loss | -76.4163 |
| avg_hold_time_bars | 19.0077 |
| exposure | 0.5574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
