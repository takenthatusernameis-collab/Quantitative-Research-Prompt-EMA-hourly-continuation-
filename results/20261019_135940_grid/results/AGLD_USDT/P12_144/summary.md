# EMA Hourly Continuation — AGLD/USDT P12_144

**Symbol:** AGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.7601 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9922 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -1.9652 |
| sortino_ratio | -0.6233 |
| max_drawdown | 0.5531 |
| cagr | -0.2515 |
| net_avg_win | 66.7818 |
| net_avg_loss | -85.7620 |
| avg_hold_time_bars | 28.8313 |
| exposure | 0.6498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
