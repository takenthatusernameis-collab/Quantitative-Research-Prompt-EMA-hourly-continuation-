# EMA Hourly Continuation — IMX/USDT P34_144

**Symbol:** IMX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.6894 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 0.9697 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -2.3367 |
| sortino_ratio | -0.7170 |
| max_drawdown | 0.5892 |
| cagr | -0.2940 |
| net_avg_win | 53.3773 |
| net_avg_loss | -77.7509 |
| avg_hold_time_bars | 19.2557 |
| exposure | 0.4226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
