# EMA Hourly Continuation — GALA/USDT P34_100

**Symbol:** GALA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.5945 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.9031 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -4.5922 |
| sortino_ratio | -1.6223 |
| max_drawdown | 0.8679 |
| cagr | -0.5457 |
| net_avg_win | 43.2950 |
| net_avg_loss | -61.4555 |
| avg_hold_time_bars | 9.7806 |
| exposure | 0.2836 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
