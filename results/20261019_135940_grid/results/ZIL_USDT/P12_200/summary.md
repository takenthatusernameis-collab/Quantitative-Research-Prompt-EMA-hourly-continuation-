# EMA Hourly Continuation — ZIL/USDT P12_200

**Symbol:** ZIL/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6552 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9552 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -2.5552 |
| sortino_ratio | -0.7017 |
| max_drawdown | 0.6003 |
| cagr | -0.2861 |
| net_avg_win | 58.6534 |
| net_avg_loss | -84.0699 |
| avg_hold_time_bars | 42.8639 |
| exposure | 0.7443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
