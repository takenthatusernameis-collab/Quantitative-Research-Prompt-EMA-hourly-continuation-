# EMA Hourly Continuation — NOT/USDT P144_200

**Symbol:** NOT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.5281 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.9025 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -4.0607 |
| sortino_ratio | -1.1646 |
| max_drawdown | 0.7517 |
| cagr | -0.4344 |
| net_avg_win | 44.3949 |
| net_avg_loss | -74.2385 |
| avg_hold_time_bars | 4.0323 |
| exposure | 0.0763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
