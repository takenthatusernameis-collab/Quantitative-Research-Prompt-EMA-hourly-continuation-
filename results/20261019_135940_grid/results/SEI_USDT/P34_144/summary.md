# EMA Hourly Continuation — SEI/USDT P34_144

**Symbol:** SEI/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.6825 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9300 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -2.5204 |
| sortino_ratio | -0.7223 |
| max_drawdown | 0.5883 |
| cagr | -0.2900 |
| net_avg_win | 62.3112 |
| net_avg_loss | -84.8994 |
| avg_hold_time_bars | 23.3438 |
| exposure | 0.4382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
