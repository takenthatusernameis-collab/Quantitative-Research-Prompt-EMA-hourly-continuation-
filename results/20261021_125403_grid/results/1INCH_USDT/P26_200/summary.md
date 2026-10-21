# EMA Hourly Continuation — 1INCH/USDT P26_200

**Symbol:** 1INCH/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.7802 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 0.9746 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -1.2966 |
| sortino_ratio | -0.3128 |
| max_drawdown | 0.3710 |
| cagr | -0.1351 |
| net_avg_win | 76.8862 |
| net_avg_loss | -96.4914 |
| avg_hold_time_bars | 48.4877 |
| exposure | 0.6281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
