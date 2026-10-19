# EMA Hourly Continuation — GRAM/USDT P89_144

**Symbol:** GRAM/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.3556 |
| net_win_rate | 0.4272 |
| gross_profit_factor | 0.7724 |
| gross_win_rate | 0.4466 |
| sharpe_ratio | -6.6247 |
| sortino_ratio | -2.1275 |
| max_drawdown | 0.9367 |
| cagr | -0.6625 |
| net_avg_win | 23.4402 |
| net_avg_loss | -49.1634 |
| avg_hold_time_bars | 4.8505 |
| exposure | 0.1135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
