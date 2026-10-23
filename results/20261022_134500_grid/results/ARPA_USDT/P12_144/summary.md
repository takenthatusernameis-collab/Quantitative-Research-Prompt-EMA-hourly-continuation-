# EMA Hourly Continuation — ARPA/USDT P12_144

**Symbol:** ARPA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.5786 |
| net_win_rate | 0.4543 |
| gross_profit_factor | 0.8510 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -4.4128 |
| sortino_ratio | -1.5396 |
| max_drawdown | 0.8506 |
| cagr | -0.5227 |
| net_avg_win | 41.0133 |
| net_avg_loss | -58.9975 |
| avg_hold_time_bars | 22.6581 |
| exposure | 0.6388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
