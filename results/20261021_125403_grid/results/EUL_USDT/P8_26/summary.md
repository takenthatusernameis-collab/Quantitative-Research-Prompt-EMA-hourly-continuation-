# EMA Hourly Continuation — EUL/USDT P8_26

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.6331 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.8502 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -3.4203 |
| sortino_ratio | -1.2676 |
| max_drawdown | 0.7848 |
| cagr | -0.4420 |
| net_avg_win | 41.9955 |
| net_avg_loss | -58.2219 |
| avg_hold_time_bars | 8.4408 |
| exposure | 0.2594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
