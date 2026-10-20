# EMA Hourly Continuation — ATH/USDT P55_200

**Symbol:** ATH/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6637 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.8853 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -2.7077 |
| sortino_ratio | -0.7631 |
| max_drawdown | 0.5866 |
| cagr | -0.3047 |
| net_avg_win | 64.4753 |
| net_avg_loss | -85.4917 |
| avg_hold_time_bars | 20.2128 |
| exposure | 0.3684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
