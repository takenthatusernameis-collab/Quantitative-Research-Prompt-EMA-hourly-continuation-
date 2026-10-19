# EMA Hourly Continuation — TAO/USDT P12_100

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.6947 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9521 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -3.2263 |
| sortino_ratio | -1.1661 |
| max_drawdown | 0.7629 |
| cagr | -0.4265 |
| net_avg_win | 54.1768 |
| net_avg_loss | -71.8502 |
| avg_hold_time_bars | 18.7997 |
| exposure | 0.5631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
