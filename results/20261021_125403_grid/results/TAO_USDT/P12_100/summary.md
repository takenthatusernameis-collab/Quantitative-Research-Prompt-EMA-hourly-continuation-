# EMA Hourly Continuation — TAO/USDT P12_100

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.9067 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0631 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -0.6861 |
| sortino_ratio | -0.2119 |
| max_drawdown | 0.3351 |
| cagr | -0.0975 |
| net_avg_win | 92.7736 |
| net_avg_loss | -108.7128 |
| avg_hold_time_bars | 26.1385 |
| exposure | 0.5489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
