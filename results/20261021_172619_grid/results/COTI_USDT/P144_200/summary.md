# EMA Hourly Continuation — COTI/USDT P144_200

**Symbol:** COTI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 177 |
| net_profit_factor | 0.8416 |
| net_win_rate | 0.5254 |
| gross_profit_factor | 1.0918 |
| gross_win_rate | 0.5254 |
| sharpe_ratio | -0.6634 |
| sortino_ratio | -0.1273 |
| max_drawdown | 0.1679 |
| cagr | -0.0577 |
| net_avg_win | 79.2657 |
| net_avg_loss | -104.2720 |
| avg_hold_time_bars | 7.4859 |
| exposure | 0.0602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
