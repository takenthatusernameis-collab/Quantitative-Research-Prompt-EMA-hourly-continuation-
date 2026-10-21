# EMA Hourly Continuation — DOGE/USDT P8_200

**Symbol:** DOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.8747 |
| net_win_rate | 0.5171 |
| gross_profit_factor | 1.0684 |
| gross_win_rate | 0.5171 |
| sharpe_ratio | -0.6595 |
| sortino_ratio | -0.1534 |
| max_drawdown | 0.1993 |
| cagr | -0.0706 |
| net_avg_win | 86.1687 |
| net_avg_loss | -105.4961 |
| avg_hold_time_bars | 65.9125 |
| exposure | 0.7880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
