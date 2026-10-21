# EMA Hourly Continuation — KAS/USDT P20_89

**Symbol:** KAS/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.8116 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0195 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -1.3464 |
| sortino_ratio | -0.4248 |
| max_drawdown | 0.4143 |
| cagr | -0.1786 |
| net_avg_win | 68.2790 |
| net_avg_loss | -87.3259 |
| avg_hold_time_bars | 15.8012 |
| exposure | 0.3469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
