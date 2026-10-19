# EMA Hourly Continuation — GRAM/USDT P20_34

**Symbol:** GRAM/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1178 |
| net_profit_factor | 0.2436 |
| net_win_rate | 0.3820 |
| gross_profit_factor | 0.6721 |
| gross_win_rate | 0.4202 |
| sharpe_ratio | -13.5320 |
| sortino_ratio | -6.7158 |
| max_drawdown | 0.9999 |
| cagr | -0.9715 |
| net_avg_win | 7.1550 |
| net_avg_loss | -18.1572 |
| avg_hold_time_bars | 2.4525 |
| exposure | 0.1313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
