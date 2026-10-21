# EMA Hourly Continuation — IMX/USDT P100_144

**Symbol:** IMX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.7842 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0403 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -1.1672 |
| sortino_ratio | -0.2697 |
| max_drawdown | 0.3259 |
| cagr | -0.1167 |
| net_avg_win | 73.4635 |
| net_avg_loss | -98.8784 |
| avg_hold_time_bars | 6.5560 |
| exposure | 0.0768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
