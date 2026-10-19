# EMA Hourly Continuation — ZEC/USDT P12_144

**Symbol:** ZEC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.8245 |
| net_win_rate | 0.5281 |
| gross_profit_factor | 1.1326 |
| gross_win_rate | 0.5371 |
| sharpe_ratio | -1.1089 |
| sortino_ratio | -0.3320 |
| max_drawdown | 0.3525 |
| cagr | -0.1477 |
| net_avg_win | 66.0852 |
| net_avg_loss | -89.6940 |
| avg_hold_time_bars | 33.7933 |
| exposure | 0.6835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
