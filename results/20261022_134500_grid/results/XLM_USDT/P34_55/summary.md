# EMA Hourly Continuation — XLM/USDT P34_55

**Symbol:** XLM/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 877 |
| net_profit_factor | 0.2233 |
| net_win_rate | 0.4287 |
| gross_profit_factor | 0.6999 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -9.5830 |
| sortino_ratio | -4.0596 |
| max_drawdown | 0.9945 |
| cagr | -0.8729 |
| net_avg_win | 7.6031 |
| net_avg_loss | -25.5538 |
| avg_hold_time_bars | 3.2702 |
| exposure | 0.1304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
