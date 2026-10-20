# EMA Hourly Continuation — XPR/USDT P26_144

**Symbol:** XPR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.4553 |
| net_win_rate | 0.4400 |
| gross_profit_factor | 0.7254 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -4.7684 |
| sortino_ratio | -1.4942 |
| max_drawdown | 0.8447 |
| cagr | -0.5159 |
| net_avg_win | 31.8506 |
| net_avg_loss | -54.9625 |
| avg_hold_time_bars | 19.6700 |
| exposure | 0.4470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
