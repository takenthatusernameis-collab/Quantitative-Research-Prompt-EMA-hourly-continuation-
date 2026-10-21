# EMA Hourly Continuation — FET/USDT P20_34

**Symbol:** FET/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.8360 |
| net_win_rate | 0.5205 |
| gross_profit_factor | 1.0690 |
| gross_win_rate | 0.5205 |
| sharpe_ratio | -0.8031 |
| sortino_ratio | -0.1807 |
| max_drawdown | 0.2621 |
| cagr | -0.0807 |
| net_avg_win | 76.4879 |
| net_avg_loss | -99.3087 |
| avg_hold_time_bars | 5.7254 |
| exposure | 0.0635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
