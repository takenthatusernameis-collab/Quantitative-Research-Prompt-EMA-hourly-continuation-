# EMA Hourly Continuation — AUCTION/USDT P26_34

**Symbol:** AUCTION/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1035 |
| net_profit_factor | 0.2783 |
| net_win_rate | 0.3729 |
| gross_profit_factor | 0.7361 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -12.3460 |
| sortino_ratio | -5.7329 |
| max_drawdown | 0.9994 |
| cagr | -0.9482 |
| net_avg_win | 9.9826 |
| net_avg_loss | -21.3368 |
| avg_hold_time_bars | 3.2831 |
| exposure | 0.1538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
