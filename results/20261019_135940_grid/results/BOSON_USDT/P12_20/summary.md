# EMA Hourly Continuation — BOSON/USDT P12_20

**Symbol:** BOSON/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1217 |
| net_profit_factor | 0.3779 |
| net_win_rate | 0.4166 |
| gross_profit_factor | 0.8025 |
| gross_win_rate | 0.4363 |
| sharpe_ratio | -10.2709 |
| sortino_ratio | -5.0468 |
| max_drawdown | 0.9982 |
| cagr | -0.9194 |
| net_avg_win | 11.9621 |
| net_avg_loss | -22.6012 |
| avg_hold_time_bars | 3.1972 |
| exposure | 0.1769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
