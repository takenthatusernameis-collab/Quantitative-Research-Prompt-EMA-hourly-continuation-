# EMA Hourly Continuation — CVX/USDT P20_144

**Symbol:** CVX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.6012 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8402 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -3.3511 |
| sortino_ratio | -0.9966 |
| max_drawdown | 0.7074 |
| cagr | -0.3813 |
| net_avg_win | 51.7561 |
| net_avg_loss | -71.3959 |
| avg_hold_time_bars | 27.8511 |
| exposure | 0.5697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
