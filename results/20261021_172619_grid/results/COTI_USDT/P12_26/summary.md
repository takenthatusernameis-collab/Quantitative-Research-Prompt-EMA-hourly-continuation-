# EMA Hourly Continuation — COTI/USDT P12_26

**Symbol:** COTI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.8069 |
| net_win_rate | 0.5196 |
| gross_profit_factor | 1.0715 |
| gross_win_rate | 0.5196 |
| sharpe_ratio | -1.3664 |
| sortino_ratio | -0.4095 |
| max_drawdown | 0.4384 |
| cagr | -0.1721 |
| net_avg_win | 70.1347 |
| net_avg_loss | -94.0209 |
| avg_hold_time_bars | 5.5150 |
| exposure | 0.1085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
