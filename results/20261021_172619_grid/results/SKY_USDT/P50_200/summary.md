# EMA Hourly Continuation — SKY/USDT P50_200

**Symbol:** SKY/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.8527 |
| net_win_rate | 0.5162 |
| gross_profit_factor | 1.0585 |
| gross_win_rate | 0.5162 |
| sharpe_ratio | -0.9174 |
| sortino_ratio | -0.2426 |
| max_drawdown | 0.3631 |
| cagr | -0.1078 |
| net_avg_win | 84.3558 |
| net_avg_loss | -105.5679 |
| avg_hold_time_bars | 23.3069 |
| exposure | 0.3600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
