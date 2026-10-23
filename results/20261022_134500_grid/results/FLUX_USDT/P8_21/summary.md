# EMA Hourly Continuation — FLUX/USDT P8_21

**Symbol:** FLUX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1623 |
| net_profit_factor | 0.4707 |
| net_win_rate | 0.4584 |
| gross_profit_factor | 1.0271 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -10.2005 |
| sortino_ratio | -5.7870 |
| max_drawdown | 0.9994 |
| cagr | -0.9451 |
| net_avg_win | 11.9455 |
| net_avg_loss | -21.4796 |
| avg_hold_time_bars | 2.9137 |
| exposure | 0.2150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
