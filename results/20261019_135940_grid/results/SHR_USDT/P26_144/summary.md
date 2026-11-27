# EMA Hourly Continuation — SHR/USDT P26_144

**Symbol:** SHR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 803 |
| net_profit_factor | 0.4283 |
| net_win_rate | 0.3375 |
| gross_profit_factor | 0.5729 |
| gross_win_rate | 0.3387 |
| sharpe_ratio | -8.0187 |
| sortino_ratio | -3.1643 |
| max_drawdown | 0.9787 |
| cagr | -0.7801 |
| net_avg_win | 27.0371 |
| net_avg_loss | -32.1577 |
| avg_hold_time_bars | 10.8244 |
| exposure | 0.3933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
