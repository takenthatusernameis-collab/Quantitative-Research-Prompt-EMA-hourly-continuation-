# EMA Hourly Continuation — QI/USDT P34_200

**Symbol:** QI/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.7340 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9229 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -1.7224 |
| sortino_ratio | -0.4465 |
| max_drawdown | 0.4332 |
| cagr | -0.1863 |
| net_avg_win | 69.9294 |
| net_avg_loss | -88.6297 |
| avg_hold_time_bars | 28.9548 |
| exposure | 0.4350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
