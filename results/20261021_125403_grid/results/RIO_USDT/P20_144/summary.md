# EMA Hourly Continuation — RIO/USDT P20_144

**Symbol:** RIO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.8108 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9116 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -1.4506 |
| sortino_ratio | -0.4329 |
| max_drawdown | 0.4581 |
| cagr | -0.1830 |
| net_avg_win | 81.4058 |
| net_avg_loss | -91.1907 |
| avg_hold_time_bars | 24.9153 |
| exposure | 0.4999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
