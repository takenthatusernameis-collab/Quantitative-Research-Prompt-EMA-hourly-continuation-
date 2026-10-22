# EMA Hourly Continuation — TAO/USDT P21_144

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.7152 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9921 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -2.5294 |
| sortino_ratio | -0.7786 |
| max_drawdown | 0.6370 |
| cagr | -0.3139 |
| net_avg_win | 64.5317 |
| net_avg_loss | -87.2983 |
| avg_hold_time_bars | 23.9979 |
| exposure | 0.5280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
