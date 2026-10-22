# EMA Hourly Continuation — POKT/USDT P20_34

**Symbol:** POKT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.4972 |
| net_win_rate | 0.3747 |
| gross_profit_factor | 0.6863 |
| gross_win_rate | 0.3793 |
| sharpe_ratio | -5.2463 |
| sortino_ratio | -1.5447 |
| max_drawdown | 0.8391 |
| cagr | -0.5129 |
| net_avg_win | 50.7774 |
| net_avg_loss | -61.2043 |
| avg_hold_time_bars | 6.2828 |
| exposure | 0.1237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
