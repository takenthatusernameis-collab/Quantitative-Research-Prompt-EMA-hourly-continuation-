# EMA Hourly Continuation — SUI/USDT P20_200

**Symbol:** SUI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.9404 |
| net_win_rate | 0.5233 |
| gross_profit_factor | 1.0915 |
| gross_win_rate | 0.5233 |
| sharpe_ratio | -0.2702 |
| sortino_ratio | -0.0650 |
| max_drawdown | 0.1898 |
| cagr | -0.0334 |
| net_avg_win | 88.4417 |
| net_avg_loss | -103.2415 |
| avg_hold_time_bars | 50.1290 |
| exposure | 0.6357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
