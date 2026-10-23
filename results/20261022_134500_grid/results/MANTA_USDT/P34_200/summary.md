# EMA Hourly Continuation — MANTA/USDT P34_200

**Symbol:** MANTA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.7412 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9316 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -1.8111 |
| sortino_ratio | -0.4645 |
| max_drawdown | 0.4464 |
| cagr | -0.1934 |
| net_avg_win | 76.5736 |
| net_avg_loss | -94.8036 |
| avg_hold_time_bars | 37.3006 |
| exposure | 0.5527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
