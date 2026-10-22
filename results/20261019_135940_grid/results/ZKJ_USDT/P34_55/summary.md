# EMA Hourly Continuation — ZKJ/USDT P34_55

**Symbol:** ZKJ/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1027 |
| net_profit_factor | 0.1329 |
| net_win_rate | 0.2386 |
| gross_profit_factor | 0.4327 |
| gross_win_rate | 0.3340 |
| sharpe_ratio | -17.0027 |
| sortino_ratio | -8.2102 |
| max_drawdown | 1.0000 |
| cagr | -0.9890 |
| net_avg_win | 6.2559 |
| net_avg_loss | -14.7475 |
| avg_hold_time_bars | 6.4615 |
| exposure | 0.3016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
