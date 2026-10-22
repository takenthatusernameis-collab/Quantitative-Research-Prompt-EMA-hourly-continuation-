# EMA Hourly Continuation — FLUX/USDT P26_55

**Symbol:** FLUX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.6742 |
| net_win_rate | 0.4703 |
| gross_profit_factor | 0.9032 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -2.6624 |
| sortino_ratio | -0.7804 |
| max_drawdown | 0.6161 |
| cagr | -0.3006 |
| net_avg_win | 61.9452 |
| net_avg_loss | -81.5755 |
| avg_hold_time_bars | 6.5036 |
| exposure | 0.1245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
