# EMA Hourly Continuation — FLOKI/USDT P8_34

**Symbol:** FLOKI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.7437 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9379 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -2.6502 |
| sortino_ratio | -1.0037 |
| max_drawdown | 0.7000 |
| cagr | -0.3692 |
| net_avg_win | 58.5207 |
| net_avg_loss | -73.7008 |
| avg_hold_time_bars | 8.6956 |
| exposure | 0.2779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
