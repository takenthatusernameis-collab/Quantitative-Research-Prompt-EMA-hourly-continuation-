# EMA Hourly Continuation — SHIB/USDT P20_55

**Symbol:** SHIB/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 978 |
| net_profit_factor | 0.4801 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.9358 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -7.4709 |
| sortino_ratio | -3.2919 |
| max_drawdown | 0.9836 |
| cagr | -0.8019 |
| net_avg_win | 20.3468 |
| net_avg_loss | -35.5321 |
| avg_hold_time_bars | 4.6718 |
| exposure | 0.2077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
