# EMA Hourly Continuation — ETC/USDT P12_100

**Symbol:** ETC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6858 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9274 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -2.6730 |
| sortino_ratio | -0.8467 |
| max_drawdown | 0.6364 |
| cagr | -0.3214 |
| net_avg_win | 57.3073 |
| net_avg_loss | -77.3624 |
| avg_hold_time_bars | 23.3651 |
| exposure | 0.5236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
