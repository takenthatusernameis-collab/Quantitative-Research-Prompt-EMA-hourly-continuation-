# EMA Hourly Continuation — BCH/USDT P8_100

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.5988 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 1.0119 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -4.8380 |
| sortino_ratio | -1.7538 |
| max_drawdown | 0.8930 |
| cagr | -0.5798 |
| net_avg_win | 41.4880 |
| net_avg_loss | -62.6095 |
| avg_hold_time_bars | 21.5714 |
| exposure | 0.6589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
