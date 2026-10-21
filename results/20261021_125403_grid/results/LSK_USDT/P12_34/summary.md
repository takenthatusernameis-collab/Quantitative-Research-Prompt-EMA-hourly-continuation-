# EMA Hourly Continuation — LSK/USDT P12_34

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.6613 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 0.9735 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -4.1699 |
| sortino_ratio | -1.5674 |
| max_drawdown | 0.8455 |
| cagr | -0.5138 |
| net_avg_win | 50.4066 |
| net_avg_loss | -67.1107 |
| avg_hold_time_bars | 6.9884 |
| exposure | 0.2198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
