# EMA Hourly Continuation — YGG/USDT P8_50

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 773 |
| net_profit_factor | 0.7979 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9867 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -2.3710 |
| sortino_ratio | -0.9394 |
| max_drawdown | 0.6939 |
| cagr | -0.3515 |
| net_avg_win | 69.4026 |
| net_avg_loss | -83.2433 |
| avg_hold_time_bars | 12.2988 |
| exposure | 0.4302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
