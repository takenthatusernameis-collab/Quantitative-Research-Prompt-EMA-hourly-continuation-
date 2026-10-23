# EMA Hourly Continuation — SKL/USDT P12_100

**Symbol:** SKL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.7842 |
| net_win_rate | 0.5096 |
| gross_profit_factor | 1.0946 |
| gross_win_rate | 0.5176 |
| sharpe_ratio | -2.2214 |
| sortino_ratio | -0.7922 |
| max_drawdown | 0.6737 |
| cagr | -0.3093 |
| net_avg_win | 68.9427 |
| net_avg_loss | -91.3492 |
| avg_hold_time_bars | 21.2252 |
| exposure | 0.6040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
