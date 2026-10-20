# EMA Hourly Continuation — TFUEL/USDT P50_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.4478 |
| net_win_rate | 0.3952 |
| gross_profit_factor | 0.7209 |
| gross_win_rate | 0.4048 |
| sharpe_ratio | -6.7384 |
| sortino_ratio | -2.3775 |
| max_drawdown | 0.9447 |
| cagr | -0.6815 |
| net_avg_win | 30.9945 |
| net_avg_loss | -45.2326 |
| avg_hold_time_bars | 9.5424 |
| exposure | 0.2699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
