# EMA Hourly Continuation — ZKJ/USDT P21_34

**Symbol:** ZKJ/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1346 |
| net_profit_factor | 0.1508 |
| net_win_rate | 0.2578 |
| gross_profit_factor | 0.4466 |
| gross_win_rate | 0.3484 |
| sharpe_ratio | -19.2089 |
| sortino_ratio | -10.5907 |
| max_drawdown | 1.0000 |
| cagr | -0.9971 |
| net_avg_win | 5.1170 |
| net_avg_loss | -11.7874 |
| avg_hold_time_bars | 3.4450 |
| exposure | 0.2108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
