# EMA Hourly Continuation — SKY/USDT P8_144

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.8670 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0546 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -0.9099 |
| sortino_ratio | -0.2647 |
| max_drawdown | 0.4411 |
| cagr | -0.1176 |
| net_avg_win | 85.1382 |
| net_avg_loss | -104.2190 |
| avg_hold_time_bars | 37.0089 |
| exposure | 0.6934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
