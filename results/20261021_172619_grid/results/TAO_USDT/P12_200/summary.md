# EMA Hourly Continuation — TAO/USDT P12_200

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.9759 |
| net_win_rate | 0.5265 |
| gross_profit_factor | 1.1080 |
| gross_win_rate | 0.5265 |
| sharpe_ratio | -0.0832 |
| sortino_ratio | -0.0202 |
| max_drawdown | 0.1408 |
| cagr | -0.0143 |
| net_avg_win | 96.8462 |
| net_avg_loss | -110.3466 |
| avg_hold_time_bars | 57.5265 |
| exposure | 0.7400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
