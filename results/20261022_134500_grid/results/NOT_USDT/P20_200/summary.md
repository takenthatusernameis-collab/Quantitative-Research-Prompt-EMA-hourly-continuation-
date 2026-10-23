# EMA Hourly Continuation — NOT/USDT P20_200

**Symbol:** NOT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.5372 |
| net_win_rate | 0.4204 |
| gross_profit_factor | 0.7331 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -3.8656 |
| sortino_ratio | -1.0757 |
| max_drawdown | 0.7257 |
| cagr | -0.4035 |
| net_avg_win | 51.5523 |
| net_avg_loss | -69.5988 |
| avg_hold_time_bars | 35.3211 |
| exposure | 0.6355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
