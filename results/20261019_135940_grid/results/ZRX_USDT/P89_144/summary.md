# EMA Hourly Continuation — ZRX/USDT P89_144

**Symbol:** ZRX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.4878 |
| net_win_rate | 0.4506 |
| gross_profit_factor | 0.9223 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -5.3350 |
| sortino_ratio | -1.7253 |
| max_drawdown | 0.8818 |
| cagr | -0.5722 |
| net_avg_win | 35.4118 |
| net_avg_loss | -59.5388 |
| avg_hold_time_bars | 4.8745 |
| exposure | 0.1165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
