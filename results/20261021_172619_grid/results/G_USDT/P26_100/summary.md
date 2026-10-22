# EMA Hourly Continuation — G/USDT P26_100

**Symbol:** G/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.5968 |
| net_win_rate | 0.4387 |
| gross_profit_factor | 0.7805 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -3.5361 |
| sortino_ratio | -1.0899 |
| max_drawdown | 0.6954 |
| cagr | -0.3955 |
| net_avg_win | 54.9664 |
| net_avg_loss | -71.9891 |
| avg_hold_time_bars | 18.5686 |
| exposure | 0.3984 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
