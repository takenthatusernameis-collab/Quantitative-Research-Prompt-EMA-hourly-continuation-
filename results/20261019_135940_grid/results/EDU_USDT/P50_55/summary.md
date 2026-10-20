# EMA Hourly Continuation — EDU/USDT P50_55

**Symbol:** EDU/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 828 |
| net_profit_factor | 0.2545 |
| net_win_rate | 0.3696 |
| gross_profit_factor | 0.6703 |
| gross_win_rate | 0.4203 |
| sharpe_ratio | -10.9179 |
| sortino_ratio | -4.5398 |
| max_drawdown | 0.9973 |
| cagr | -0.9038 |
| net_avg_win | 11.1281 |
| net_avg_loss | -25.6283 |
| avg_hold_time_bars | 2.4626 |
| exposure | 0.0923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
