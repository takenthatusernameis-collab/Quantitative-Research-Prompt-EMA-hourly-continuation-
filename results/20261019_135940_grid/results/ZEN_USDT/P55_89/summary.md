# EMA Hourly Continuation — ZEN/USDT P55_89

**Symbol:** ZEN/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.4911 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.9007 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -6.1089 |
| sortino_ratio | -2.3544 |
| max_drawdown | 0.9426 |
| cagr | -0.6785 |
| net_avg_win | 27.5494 |
| net_avg_loss | -45.1528 |
| avg_hold_time_bars | 4.0811 |
| exposure | 0.1373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
