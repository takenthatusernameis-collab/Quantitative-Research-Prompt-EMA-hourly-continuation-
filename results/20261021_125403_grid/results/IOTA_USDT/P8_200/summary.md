# EMA Hourly Continuation — IOTA/USDT P8_200

**Symbol:** IOTA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.9393 |
| net_win_rate | 0.5298 |
| gross_profit_factor | 1.1229 |
| gross_win_rate | 0.5298 |
| sharpe_ratio | -0.2899 |
| sortino_ratio | -0.0726 |
| max_drawdown | 0.2149 |
| cagr | -0.0371 |
| net_avg_win | 87.4976 |
| net_avg_loss | -104.9629 |
| avg_hold_time_bars | 58.6821 |
| exposure | 0.8055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
