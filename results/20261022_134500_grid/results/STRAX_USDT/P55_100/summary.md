# EMA Hourly Continuation — STRAX/USDT P55_100

**Symbol:** STRAX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.4708 |
| net_win_rate | 0.4144 |
| gross_profit_factor | 0.8493 |
| gross_win_rate | 0.4414 |
| sharpe_ratio | -7.4018 |
| sortino_ratio | -2.6836 |
| max_drawdown | 0.9668 |
| cagr | -0.7443 |
| net_avg_win | 31.1646 |
| net_avg_loss | -46.8441 |
| avg_hold_time_bars | 5.8243 |
| exposure | 0.1774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
