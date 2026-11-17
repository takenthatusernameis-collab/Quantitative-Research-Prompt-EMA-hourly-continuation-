# EMA Hourly Continuation — NUM/USDT P8_89

**Symbol:** NUM/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 797 |
| net_profit_factor | 0.5559 |
| net_win_rate | 0.4015 |
| gross_profit_factor | 0.8056 |
| gross_win_rate | 0.4078 |
| sharpe_ratio | -6.3509 |
| sortino_ratio | -2.5186 |
| max_drawdown | 0.9541 |
| cagr | -0.6966 |
| net_avg_win | 37.1591 |
| net_avg_loss | -44.8438 |
| avg_hold_time_bars | 16.0402 |
| exposure | 0.5811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
