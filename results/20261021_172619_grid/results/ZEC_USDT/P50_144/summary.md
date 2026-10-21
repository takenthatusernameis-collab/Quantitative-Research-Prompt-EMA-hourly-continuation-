# EMA Hourly Continuation — ZEC/USDT P50_144

**Symbol:** ZEC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.8979 |
| net_win_rate | 0.5223 |
| gross_profit_factor | 1.0902 |
| gross_win_rate | 0.5223 |
| sharpe_ratio | -0.5641 |
| sortino_ratio | -0.1491 |
| max_drawdown | 0.2512 |
| cagr | -0.0694 |
| net_avg_win | 82.6160 |
| net_avg_loss | -100.5799 |
| avg_hold_time_bars | 15.9674 |
| exposure | 0.2446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
