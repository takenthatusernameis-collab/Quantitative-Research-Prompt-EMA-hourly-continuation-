# EMA Hourly Continuation — SUSHI/USDT P12_200

**Symbol:** SUSHI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.7740 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9197 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -1.2888 |
| sortino_ratio | -0.3058 |
| max_drawdown | 0.3085 |
| cagr | -0.1319 |
| net_avg_win | 76.7017 |
| net_avg_loss | -91.5763 |
| avg_hold_time_bars | 58.8817 |
| exposure | 0.7434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
