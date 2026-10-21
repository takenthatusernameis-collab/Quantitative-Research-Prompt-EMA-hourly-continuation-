# EMA Hourly Continuation — LISTA/USDT P8_100

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.8788 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0375 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -0.9279 |
| sortino_ratio | -0.3003 |
| max_drawdown | 0.3422 |
| cagr | -0.1326 |
| net_avg_win | 85.0206 |
| net_avg_loss | -100.0686 |
| avg_hold_time_bars | 27.0253 |
| exposure | 0.6264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
