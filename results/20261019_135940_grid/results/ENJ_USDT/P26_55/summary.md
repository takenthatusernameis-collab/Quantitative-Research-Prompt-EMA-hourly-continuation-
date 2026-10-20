# EMA Hourly Continuation — ENJ/USDT P26_55

**Symbol:** ENJ/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 955 |
| net_profit_factor | 0.5401 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 1.0305 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -7.1114 |
| sortino_ratio | -3.1044 |
| max_drawdown | 0.9794 |
| cagr | -0.7825 |
| net_avg_win | 26.1707 |
| net_avg_loss | -41.2247 |
| avg_hold_time_bars | 4.1079 |
| exposure | 0.1783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
