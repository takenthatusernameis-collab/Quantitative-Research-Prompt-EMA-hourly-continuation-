# EMA Hourly Continuation — BOME/USDT P100_144

**Symbol:** BOME/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.6815 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.8687 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -1.7332 |
| sortino_ratio | -0.3902 |
| max_drawdown | 0.3815 |
| cagr | -0.1636 |
| net_avg_win | 65.5555 |
| net_avg_loss | -86.6492 |
| avg_hold_time_bars | 6.1687 |
| exposure | 0.0698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
