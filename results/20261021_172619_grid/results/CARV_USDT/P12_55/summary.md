# EMA Hourly Continuation — CARV/USDT P12_55

**Symbol:** CARV/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.7803 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0207 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -1.9798 |
| sortino_ratio | -0.7325 |
| max_drawdown | 0.5044 |
| cagr | -0.2867 |
| net_avg_win | 64.7689 |
| net_avg_loss | -84.8790 |
| avg_hold_time_bars | 12.9721 |
| exposure | 0.3927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
