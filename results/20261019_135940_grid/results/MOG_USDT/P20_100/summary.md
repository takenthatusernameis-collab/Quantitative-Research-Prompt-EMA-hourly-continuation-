# EMA Hourly Continuation — MOG/USDT P20_100

**Symbol:** MOG/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.6765 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.8710 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -3.5071 |
| sortino_ratio | -1.2642 |
| max_drawdown | 0.7683 |
| cagr | -0.4478 |
| net_avg_win | 56.3960 |
| net_avg_loss | -71.8988 |
| avg_hold_time_bars | 14.2802 |
| exposure | 0.4231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
