# EMA Hourly Continuation — DBR/USDT P26_55

**Symbol:** DBR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.4479 |
| net_win_rate | 0.4229 |
| gross_profit_factor | 0.8815 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -7.5062 |
| sortino_ratio | -2.8534 |
| max_drawdown | 0.9430 |
| cagr | -0.7547 |
| net_avg_win | 31.2620 |
| net_avg_loss | -51.1480 |
| avg_hold_time_bars | 6.6828 |
| exposure | 0.2193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
