# EMA Hourly Continuation — ZRX/USDT P55_89

**Symbol:** ZRX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.6580 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9700 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -2.5823 |
| sortino_ratio | -0.7260 |
| max_drawdown | 0.5926 |
| cagr | -0.2819 |
| net_avg_win | 57.1780 |
| net_avg_loss | -85.1013 |
| avg_hold_time_bars | 6.1979 |
| exposure | 0.1082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
