# EMA Hourly Continuation — QI/USDT P55_144

**Symbol:** QI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.6563 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8616 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -2.3344 |
| sortino_ratio | -0.6230 |
| max_drawdown | 0.5184 |
| cagr | -0.2488 |
| net_avg_win | 59.4944 |
| net_avg_loss | -79.5638 |
| avg_hold_time_bars | 14.0652 |
| exposure | 0.2247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
