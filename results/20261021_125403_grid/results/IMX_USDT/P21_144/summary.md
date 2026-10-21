# EMA Hourly Continuation — IMX/USDT P21_144

**Symbol:** IMX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.8361 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 0.9853 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -0.9472 |
| sortino_ratio | -0.2626 |
| max_drawdown | 0.3091 |
| cagr | -0.1164 |
| net_avg_win | 72.3454 |
| net_avg_loss | -86.9901 |
| avg_hold_time_bars | 32.4191 |
| exposure | 0.5531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
