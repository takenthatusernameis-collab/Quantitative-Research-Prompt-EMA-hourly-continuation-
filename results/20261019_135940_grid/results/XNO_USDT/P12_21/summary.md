# EMA Hourly Continuation — XNO/USDT P12_21

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1604 |
| net_profit_factor | 0.2291 |
| net_win_rate | 0.3354 |
| gross_profit_factor | 0.6359 |
| gross_win_rate | 0.3647 |
| sharpe_ratio | -16.7703 |
| sortino_ratio | -9.6726 |
| max_drawdown | 1.0000 |
| cagr | -0.9934 |
| net_avg_win | 5.5238 |
| net_avg_loss | -12.1687 |
| avg_hold_time_bars | 2.2986 |
| exposure | 0.1676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
