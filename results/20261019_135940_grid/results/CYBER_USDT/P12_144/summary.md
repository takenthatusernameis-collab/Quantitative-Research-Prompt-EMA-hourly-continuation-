# EMA Hourly Continuation — CYBER/USDT P12_144

**Symbol:** CYBER/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.7617 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0462 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.9636 |
| sortino_ratio | -0.5904 |
| max_drawdown | 0.5234 |
| cagr | -0.2479 |
| net_avg_win | 70.7075 |
| net_avg_loss | -93.6377 |
| avg_hold_time_bars | 32.8587 |
| exposure | 0.6870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
