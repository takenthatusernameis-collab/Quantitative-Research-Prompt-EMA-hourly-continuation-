# EMA Hourly Continuation — TAO/USDT P100_144

**Symbol:** TAO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.5213 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.9274 |
| gross_win_rate | 0.4574 |
| sharpe_ratio | -5.4383 |
| sortino_ratio | -1.6354 |
| max_drawdown | 0.8835 |
| cagr | -0.5736 |
| net_avg_win | 45.9835 |
| net_avg_loss | -70.6310 |
| avg_hold_time_bars | 3.3404 |
| exposure | 0.0714 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
