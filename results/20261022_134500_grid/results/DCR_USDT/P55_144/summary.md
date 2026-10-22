# EMA Hourly Continuation — DCR/USDT P55_144

**Symbol:** DCR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.5166 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 0.8423 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -4.7699 |
| sortino_ratio | -1.5630 |
| max_drawdown | 0.8530 |
| cagr | -0.5313 |
| net_avg_win | 37.4774 |
| net_avg_loss | -57.9881 |
| avg_hold_time_bars | 10.0110 |
| exposure | 0.2478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
