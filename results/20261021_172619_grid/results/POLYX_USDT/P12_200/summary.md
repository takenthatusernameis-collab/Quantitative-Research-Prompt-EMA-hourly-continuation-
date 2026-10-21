# EMA Hourly Continuation — POLYX/USDT P12_200

**Symbol:** POLYX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.8515 |
| net_win_rate | 0.5132 |
| gross_profit_factor | 1.0300 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -0.8094 |
| sortino_ratio | -0.2020 |
| max_drawdown | 0.2741 |
| cagr | -0.0910 |
| net_avg_win | 78.3261 |
| net_avg_loss | -96.9574 |
| avg_hold_time_bars | 53.0757 |
| exposure | 0.7334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
