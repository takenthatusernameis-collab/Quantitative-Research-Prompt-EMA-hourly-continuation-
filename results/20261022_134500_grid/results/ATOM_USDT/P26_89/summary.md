# EMA Hourly Continuation — ATOM/USDT P26_89

**Symbol:** ATOM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.5274 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9018 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -4.3038 |
| sortino_ratio | -1.5630 |
| max_drawdown | 0.8603 |
| cagr | -0.5313 |
| net_avg_win | 29.2172 |
| net_avg_loss | -52.6444 |
| avg_hold_time_bars | 10.6177 |
| exposure | 0.3219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
