# EMA Hourly Continuation — RSR/USDT P89_144

**Symbol:** RSR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.9785 |
| net_win_rate | 0.5543 |
| gross_profit_factor | 1.2339 |
| gross_win_rate | 0.5543 |
| sharpe_ratio | -0.0678 |
| sortino_ratio | -0.0164 |
| max_drawdown | 0.1433 |
| cagr | -0.0125 |
| net_avg_win | 92.6941 |
| net_avg_loss | -117.8362 |
| avg_hold_time_bars | 7.9275 |
| exposure | 0.0995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
