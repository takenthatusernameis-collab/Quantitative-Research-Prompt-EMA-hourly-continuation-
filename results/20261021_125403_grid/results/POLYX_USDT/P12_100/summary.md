# EMA Hourly Continuation — POLYX/USDT P12_100

**Symbol:** POLYX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.8557 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0816 |
| gross_win_rate | 0.5191 |
| sharpe_ratio | -1.2105 |
| sortino_ratio | -0.3975 |
| max_drawdown | 0.4397 |
| cagr | -0.1701 |
| net_avg_win | 81.8052 |
| net_avg_loss | -102.4039 |
| avg_hold_time_bars | 23.3683 |
| exposure | 0.5566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
