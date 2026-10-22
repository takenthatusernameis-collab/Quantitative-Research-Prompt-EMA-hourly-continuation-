# EMA Hourly Continuation — BSV/USDT P21_144

**Symbol:** BSV/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.5253 |
| net_win_rate | 0.4303 |
| gross_profit_factor | 0.8226 |
| gross_win_rate | 0.4475 |
| sharpe_ratio | -5.0952 |
| sortino_ratio | -1.7131 |
| max_drawdown | 0.8776 |
| cagr | -0.5651 |
| net_avg_win | 38.7986 |
| net_avg_loss | -55.7826 |
| avg_hold_time_bars | 20.3236 |
| exposure | 0.5367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
