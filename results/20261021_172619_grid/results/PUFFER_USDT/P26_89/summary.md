# EMA Hourly Continuation — PUFFER/USDT P26_89

**Symbol:** PUFFER/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.9123 |
| net_win_rate | 0.5293 |
| gross_profit_factor | 1.1111 |
| gross_win_rate | 0.5293 |
| sharpe_ratio | -0.5437 |
| sortino_ratio | -0.1698 |
| max_drawdown | 0.2062 |
| cagr | -0.0802 |
| net_avg_win | 81.1233 |
| net_avg_loss | -99.9735 |
| avg_hold_time_bars | 14.8963 |
| exposure | 0.3170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
