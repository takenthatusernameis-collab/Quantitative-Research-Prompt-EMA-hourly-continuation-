# EMA Hourly Continuation — FLOKI/USDT P20_144

**Symbol:** FLOKI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.8962 |
| net_win_rate | 0.5145 |
| gross_profit_factor | 1.0596 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -0.6325 |
| sortino_ratio | -0.1686 |
| max_drawdown | 0.2697 |
| cagr | -0.0776 |
| net_avg_win | 89.5708 |
| net_avg_loss | -105.9285 |
| avg_hold_time_bars | 37.5145 |
| exposure | 0.5866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
