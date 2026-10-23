# EMA Hourly Continuation — DGB/USDT P34_89

**Symbol:** DGB/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 786 |
| net_profit_factor | 0.5203 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.8933 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -6.8467 |
| sortino_ratio | -2.6922 |
| max_drawdown | 0.9656 |
| cagr | -0.7369 |
| net_avg_win | 30.7011 |
| net_avg_loss | -45.2121 |
| avg_hold_time_bars | 7.1997 |
| exposure | 0.2572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
