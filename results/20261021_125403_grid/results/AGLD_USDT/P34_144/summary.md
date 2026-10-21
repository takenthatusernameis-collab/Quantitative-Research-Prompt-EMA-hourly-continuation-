# EMA Hourly Continuation — AGLD/USDT P34_144

**Symbol:** AGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.7736 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9585 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -1.9947 |
| sortino_ratio | -0.5993 |
| max_drawdown | 0.5843 |
| cagr | -0.2410 |
| net_avg_win | 80.0327 |
| net_avg_loss | -95.4293 |
| avg_hold_time_bars | 18.9148 |
| exposure | 0.3818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
