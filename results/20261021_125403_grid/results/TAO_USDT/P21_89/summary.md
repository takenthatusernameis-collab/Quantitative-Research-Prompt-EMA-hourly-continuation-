# EMA Hourly Continuation — TAO/USDT P21_89

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.9110 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0791 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -0.6019 |
| sortino_ratio | -0.1852 |
| max_drawdown | 0.3062 |
| cagr | -0.0865 |
| net_avg_win | 87.4228 |
| net_avg_loss | -104.2880 |
| avg_hold_time_bars | 15.4573 |
| exposure | 0.3211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
