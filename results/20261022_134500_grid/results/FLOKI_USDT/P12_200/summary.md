# EMA Hourly Continuation — FLOKI/USDT P12_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.7032 |
| net_win_rate | 0.4931 |
| gross_profit_factor | 0.9828 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -2.0313 |
| sortino_ratio | -0.5467 |
| max_drawdown | 0.4917 |
| cagr | -0.2273 |
| net_avg_win | 63.4541 |
| net_avg_loss | -87.7652 |
| avg_hold_time_bars | 46.2936 |
| exposure | 0.7596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
