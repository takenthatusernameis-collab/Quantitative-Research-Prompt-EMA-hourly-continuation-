# EMA Hourly Continuation — AUCTION/USDT P26_34

**Symbol:** AUCTION/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.4501 |
| net_win_rate | 0.4147 |
| gross_profit_factor | 0.7289 |
| gross_win_rate | 0.4176 |
| sharpe_ratio | -4.8617 |
| sortino_ratio | -1.2786 |
| max_drawdown | 0.7872 |
| cagr | -0.4555 |
| net_avg_win | 45.5105 |
| net_avg_loss | -71.6487 |
| avg_hold_time_bars | 6.3382 |
| exposure | 0.0975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
