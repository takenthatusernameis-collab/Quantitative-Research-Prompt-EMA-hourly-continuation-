# EMA Hourly Continuation — ENS/USDT P34_55

**Symbol:** ENS/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 939 |
| net_profit_factor | 0.4266 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.8096 |
| gross_win_rate | 0.4547 |
| sharpe_ratio | -8.7650 |
| sortino_ratio | -3.8013 |
| max_drawdown | 0.9919 |
| cagr | -0.8523 |
| net_avg_win | 18.1330 |
| net_avg_loss | -32.5152 |
| avg_hold_time_bars | 3.2226 |
| exposure | 0.1375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
