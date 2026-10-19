# EMA Hourly Continuation — WIF/USDT P100_144

**Symbol:** WIF/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.4313 |
| net_win_rate | 0.4363 |
| gross_profit_factor | 0.7513 |
| gross_win_rate | 0.4402 |
| sharpe_ratio | -5.5431 |
| sortino_ratio | -1.7544 |
| max_drawdown | 0.8892 |
| cagr | -0.5738 |
| net_avg_win | 30.5676 |
| net_avg_loss | -54.8411 |
| avg_hold_time_bars | 3.3725 |
| exposure | 0.0770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
