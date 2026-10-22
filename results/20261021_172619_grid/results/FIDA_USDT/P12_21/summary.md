# EMA Hourly Continuation — FIDA/USDT P12_21

**Symbol:** FIDA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.6127 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.8999 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -3.2023 |
| sortino_ratio | -1.0515 |
| max_drawdown | 0.7144 |
| cagr | -0.3826 |
| net_avg_win | 43.4883 |
| net_avg_loss | -67.0480 |
| avg_hold_time_bars | 5.6395 |
| exposure | 0.1345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
