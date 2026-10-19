# EMA Hourly Continuation — APE/USDT P89_100

**Symbol:** APE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.2871 |
| net_win_rate | 0.4279 |
| gross_profit_factor | 0.8340 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -8.5038 |
| sortino_ratio | -3.0598 |
| max_drawdown | 0.9813 |
| cagr | -0.7946 |
| net_avg_win | 14.7970 |
| net_avg_loss | -38.5520 |
| avg_hold_time_bars | 1.8734 |
| exposure | 0.0531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
