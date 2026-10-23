# EMA Hourly Continuation — PEOPLE/USDT P12_50

**Symbol:** PEOPLE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.5379 |
| net_win_rate | 0.4350 |
| gross_profit_factor | 0.7976 |
| gross_win_rate | 0.4388 |
| sharpe_ratio | -6.7227 |
| sortino_ratio | -3.0265 |
| max_drawdown | 0.9741 |
| cagr | -0.7652 |
| net_avg_win | 25.3118 |
| net_avg_loss | -36.2217 |
| avg_hold_time_bars | 8.0816 |
| exposure | 0.3767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
