# EMA Hourly Continuation — ADA/USDT P26_144

**Symbol:** ADA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.8268 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0259 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -1.0212 |
| sortino_ratio | -0.2663 |
| max_drawdown | 0.3212 |
| cagr | -0.1166 |
| net_avg_win | 75.6153 |
| net_avg_loss | -95.4030 |
| avg_hold_time_bars | 30.6284 |
| exposure | 0.4608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
