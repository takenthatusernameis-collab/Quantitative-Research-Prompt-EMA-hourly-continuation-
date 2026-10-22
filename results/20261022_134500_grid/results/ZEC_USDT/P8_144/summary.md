# EMA Hourly Continuation — ZEC/USDT P8_144

**Symbol:** ZEC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.7873 |
| net_win_rate | 0.5111 |
| gross_profit_factor | 1.0418 |
| gross_win_rate | 0.5160 |
| sharpe_ratio | -1.3553 |
| sortino_ratio | -0.3872 |
| max_drawdown | 0.3978 |
| cagr | -0.1691 |
| net_avg_win | 66.2053 |
| net_avg_loss | -87.8934 |
| avg_hold_time_bars | 41.7248 |
| exposure | 0.7719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
