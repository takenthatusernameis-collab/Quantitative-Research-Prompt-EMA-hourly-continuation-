# EMA Hourly Continuation — MLK/USDT P8_89

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1069 |
| net_profit_factor | 0.3901 |
| net_win_rate | 0.3312 |
| gross_profit_factor | 0.6642 |
| gross_win_rate | 0.3452 |
| sharpe_ratio | -11.7291 |
| sortino_ratio | -5.4007 |
| max_drawdown | 0.9990 |
| cagr | -0.9353 |
| net_avg_win | 18.0532 |
| net_avg_loss | -22.9103 |
| avg_hold_time_bars | 11.4256 |
| exposure | 0.5527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
