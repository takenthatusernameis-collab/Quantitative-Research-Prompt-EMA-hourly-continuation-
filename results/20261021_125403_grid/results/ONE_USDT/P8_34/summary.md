# EMA Hourly Continuation — ONE/USDT P8_34

**Symbol:** ONE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.7715 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 0.9782 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -2.1291 |
| sortino_ratio | -0.8023 |
| max_drawdown | 0.6346 |
| cagr | -0.3087 |
| net_avg_win | 59.3208 |
| net_avg_loss | -75.7864 |
| avg_hold_time_bars | 8.8586 |
| exposure | 0.2790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
