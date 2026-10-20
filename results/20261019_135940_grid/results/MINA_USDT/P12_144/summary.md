# EMA Hourly Continuation — MINA/USDT P12_144

**Symbol:** MINA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.7525 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.0368 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -2.0575 |
| sortino_ratio | -0.6555 |
| max_drawdown | 0.6032 |
| cagr | -0.2668 |
| net_avg_win | 64.7931 |
| net_avg_loss | -86.7885 |
| avg_hold_time_bars | 29.2490 |
| exposure | 0.6727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
