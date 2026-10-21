# EMA Hourly Continuation — ETH/USDT P55_144

**Symbol:** ETH/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.6736 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 0.9919 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -1.9140 |
| sortino_ratio | -0.4730 |
| max_drawdown | 0.4507 |
| cagr | -0.1945 |
| net_avg_win | 58.0670 |
| net_avg_loss | -87.3731 |
| avg_hold_time_bars | 15.5946 |
| exposure | 0.2098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
