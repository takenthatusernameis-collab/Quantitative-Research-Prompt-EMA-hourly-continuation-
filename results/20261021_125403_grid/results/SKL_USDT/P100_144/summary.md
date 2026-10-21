# EMA Hourly Continuation — SKL/USDT P100_144

**Symbol:** SKL/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 237 |
| net_profit_factor | 0.9271 |
| net_win_rate | 0.5570 |
| gross_profit_factor | 1.2441 |
| gross_win_rate | 0.5570 |
| sharpe_ratio | -0.3165 |
| sortino_ratio | -0.0709 |
| max_drawdown | 0.1683 |
| cagr | -0.0348 |
| net_avg_win | 81.9293 |
| net_avg_loss | -111.0943 |
| avg_hold_time_bars | 6.1435 |
| exposure | 0.0662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
