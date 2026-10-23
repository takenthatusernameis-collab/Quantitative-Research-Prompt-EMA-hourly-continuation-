# EMA Hourly Continuation — PUNDIX/USDT P21_89

**Symbol:** PUNDIX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.5244 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.8258 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -5.1678 |
| sortino_ratio | -1.9529 |
| max_drawdown | 0.9071 |
| cagr | -0.6068 |
| net_avg_win | 30.5818 |
| net_avg_loss | -48.6194 |
| avg_hold_time_bars | 12.3975 |
| exposure | 0.4040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
