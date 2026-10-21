# EMA Hourly Continuation — SAND/USDT P144_200

**Symbol:** SAND/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 209 |
| net_profit_factor | 0.8169 |
| net_win_rate | 0.5359 |
| gross_profit_factor | 1.1572 |
| gross_win_rate | 0.5359 |
| sharpe_ratio | -0.9138 |
| sortino_ratio | -0.1912 |
| max_drawdown | 0.2333 |
| cagr | -0.0843 |
| net_avg_win | 79.0321 |
| net_avg_loss | -111.7090 |
| avg_hold_time_bars | 6.6411 |
| exposure | 0.0631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
