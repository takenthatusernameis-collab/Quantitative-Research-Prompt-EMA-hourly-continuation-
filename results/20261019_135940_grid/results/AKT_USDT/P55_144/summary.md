# EMA Hourly Continuation — AKT/USDT P55_144

**Symbol:** AKT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.7127 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0580 |
| gross_win_rate | 0.5188 |
| sharpe_ratio | -2.2515 |
| sortino_ratio | -0.7200 |
| max_drawdown | 0.5811 |
| cagr | -0.2880 |
| net_avg_win | 54.7527 |
| net_avg_loss | -81.5289 |
| avg_hold_time_bars | 10.8535 |
| exposure | 0.2491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
