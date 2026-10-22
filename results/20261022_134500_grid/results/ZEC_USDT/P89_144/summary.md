# EMA Hourly Continuation — ZEC/USDT P89_144

**Symbol:** ZEC/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.4470 |
| net_win_rate | 0.4561 |
| gross_profit_factor | 0.7609 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -4.2044 |
| sortino_ratio | -1.2566 |
| max_drawdown | 0.7895 |
| cagr | -0.4588 |
| net_avg_win | 30.5496 |
| net_avg_loss | -57.3161 |
| avg_hold_time_bars | 5.5482 |
| exposure | 0.1150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
