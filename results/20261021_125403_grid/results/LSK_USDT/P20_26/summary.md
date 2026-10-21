# EMA Hourly Continuation — LSK/USDT P20_26

**Symbol:** LSK/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.5487 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.9505 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -4.0313 |
| sortino_ratio | -1.1666 |
| max_drawdown | 0.7476 |
| cagr | -0.4156 |
| net_avg_win | 48.1527 |
| net_avg_loss | -75.6225 |
| avg_hold_time_bars | 5.2079 |
| exposure | 0.0956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
