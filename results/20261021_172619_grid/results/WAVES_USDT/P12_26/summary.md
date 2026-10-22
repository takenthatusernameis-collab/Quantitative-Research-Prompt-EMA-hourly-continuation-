# EMA Hourly Continuation — WAVES/USDT P12_26

**Symbol:** WAVES/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.6429 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9668 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -3.1621 |
| sortino_ratio | -0.9695 |
| max_drawdown | 0.6909 |
| cagr | -0.3600 |
| net_avg_win | 54.4098 |
| net_avg_loss | -80.6531 |
| avg_hold_time_bars | 6.1138 |
| exposure | 0.1270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
