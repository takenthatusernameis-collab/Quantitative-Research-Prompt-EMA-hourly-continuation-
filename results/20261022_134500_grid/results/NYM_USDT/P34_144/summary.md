# EMA Hourly Continuation — NYM/USDT P34_144

**Symbol:** NYM/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.2768 |
| net_win_rate | 0.3409 |
| gross_profit_factor | 0.5291 |
| gross_win_rate | 0.3595 |
| sharpe_ratio | -8.0849 |
| sortino_ratio | -2.4896 |
| max_drawdown | 0.9650 |
| cagr | -0.7364 |
| net_avg_win | 22.3852 |
| net_avg_loss | -41.8253 |
| avg_hold_time_bars | 16.7273 |
| exposure | 0.3680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
