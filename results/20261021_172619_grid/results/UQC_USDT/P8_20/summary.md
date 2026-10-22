# EMA Hourly Continuation — UQC/USDT P8_20

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.3537 |
| net_win_rate | 0.2438 |
| gross_profit_factor | 0.6229 |
| gross_win_rate | 0.3002 |
| sharpe_ratio | -10.5115 |
| sortino_ratio | -3.2969 |
| max_drawdown | 0.9898 |
| cagr | -0.8353 |
| net_avg_win | 50.1397 |
| net_avg_loss | -45.6993 |
| avg_hold_time_bars | 17.1648 |
| exposure | 0.3442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
