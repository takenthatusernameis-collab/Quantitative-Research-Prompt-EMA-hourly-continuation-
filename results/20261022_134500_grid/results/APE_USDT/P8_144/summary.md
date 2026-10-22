# EMA Hourly Continuation — APE/USDT P8_144

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6596 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9246 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -2.8130 |
| sortino_ratio | -0.8287 |
| max_drawdown | 0.6306 |
| cagr | -0.3248 |
| net_avg_win | 58.1290 |
| net_avg_loss | -80.4359 |
| avg_hold_time_bars | 38.7922 |
| exposure | 0.7723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
