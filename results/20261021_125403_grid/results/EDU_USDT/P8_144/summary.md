# EMA Hourly Continuation — EDU/USDT P8_144

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.7385 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.8745 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -1.9641 |
| sortino_ratio | -0.5872 |
| max_drawdown | 0.5114 |
| cagr | -0.2378 |
| net_avg_win | 67.0306 |
| net_avg_loss | -80.0378 |
| avg_hold_time_bars | 35.7220 |
| exposure | 0.7209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
