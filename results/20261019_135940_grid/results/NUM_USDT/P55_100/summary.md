# EMA Hourly Continuation — NUM/USDT P55_100

**Symbol:** NUM/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.4419 |
| net_win_rate | 0.3829 |
| gross_profit_factor | 0.7258 |
| gross_win_rate | 0.3860 |
| sharpe_ratio | -7.0902 |
| sortino_ratio | -2.5386 |
| max_drawdown | 0.9556 |
| cagr | -0.7075 |
| net_avg_win | 30.5957 |
| net_avg_loss | -42.9673 |
| avg_hold_time_bars | 6.8589 |
| exposure | 0.2011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
