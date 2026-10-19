# EMA Hourly Continuation — HBAR/USDT P55_89

**Symbol:** HBAR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.4266 |
| net_win_rate | 0.4303 |
| gross_profit_factor | 0.8543 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -7.3221 |
| sortino_ratio | -2.6664 |
| max_drawdown | 0.9672 |
| cagr | -0.7387 |
| net_avg_win | 25.2956 |
| net_avg_loss | -44.7880 |
| avg_hold_time_bars | 3.6439 |
| exposure | 0.1093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
