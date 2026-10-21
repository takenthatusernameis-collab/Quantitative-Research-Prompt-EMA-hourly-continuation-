# EMA Hourly Continuation — HTX/USDT P26_89

**Symbol:** HTX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.4977 |
| net_win_rate | 0.4147 |
| gross_profit_factor | 0.8263 |
| gross_win_rate | 0.4168 |
| sharpe_ratio | -5.8903 |
| sortino_ratio | -1.8164 |
| max_drawdown | 0.8900 |
| cagr | -0.5803 |
| net_avg_win | 45.8364 |
| net_avg_loss | -65.2462 |
| avg_hold_time_bars | 15.9870 |
| exposure | 0.3350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
