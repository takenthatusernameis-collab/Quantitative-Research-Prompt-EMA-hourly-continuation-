# EMA Hourly Continuation — TAO/USDT P21_144

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.8663 |
| net_win_rate | 0.4986 |
| gross_profit_factor | 0.9991 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -0.8551 |
| sortino_ratio | -0.2279 |
| max_drawdown | 0.3359 |
| cagr | -0.1021 |
| net_avg_win | 88.7641 |
| net_avg_loss | -101.8722 |
| avg_hold_time_bars | 32.8473 |
| exposure | 0.5181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
