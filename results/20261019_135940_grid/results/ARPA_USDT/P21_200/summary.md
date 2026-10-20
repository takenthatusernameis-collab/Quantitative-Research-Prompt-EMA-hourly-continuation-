# EMA Hourly Continuation — ARPA/USDT P21_200

**Symbol:** ARPA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.5673 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.8433 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -3.8317 |
| sortino_ratio | -1.1646 |
| max_drawdown | 0.7945 |
| cagr | -0.4329 |
| net_avg_win | 46.1762 |
| net_avg_loss | -67.6267 |
| avg_hold_time_bars | 27.6597 |
| exposure | 0.5958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
