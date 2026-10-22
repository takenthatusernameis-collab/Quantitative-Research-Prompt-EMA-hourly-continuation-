# EMA Hourly Continuation — CVX/USDT P8_100

**Symbol:** CVX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.6720 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9248 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -2.9538 |
| sortino_ratio | -1.0821 |
| max_drawdown | 0.7268 |
| cagr | -0.3991 |
| net_avg_win | 45.3643 |
| net_avg_loss | -63.6019 |
| avg_hold_time_bars | 21.5685 |
| exposure | 0.6588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
